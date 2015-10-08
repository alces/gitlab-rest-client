#!/usr/bin/env python

'''
copy a group with all its members and projects from one gitlab server to another
'''

import getopt
import sys
from groups import Groups
from projects import Projects
from users import Users, get_user
from utils import filter_dict

def usage(msg = ''):
	mess = msg and msg or "Usage: %s -s sourceSystem -d destinationSystem -g groupName" % sys.argv[0]
	sys.stderr.write(mess + '\n')
	sys.exit(2)

'''
add members of the object in the source system to the object in the destionation system
'''
def add_members(obj, srcId, dstId):
	# delete all the existing members first (objects' creator should be here)
	for mbr in map(lambda m: m['id'], obj.get_members(dstSys, dstId)):
		obj.del_member(dstSys, dstId, mbr)
	# return an user_id in the destination system according to a given member dict from the source system
	usr = Users()
	uidByMember = lambda mbr: get_user(dstSys, usr.by_id(srcSys, mbr['id']))
	for mbr in obj.get_members(srcSys, srcId):
		obj.add_member(dstSys, dstId, uidByMember(mbr), mbr['access_level'])
	
try:
	opts = dict(getopt.getopt(sys.argv[1:], 'hs:d:g:')[0])
except getopt.GetoptError:
	usage()

if '-h' in opts:
	usage()

try:
	srcSys = opts['-s']
	dstSys = opts['-d']
	grpNam = opts['-g']
except KeyError:
	usage()

# create a group itself	
grp = Groups()
try:
	srcGid = grp.by_name(srcSys, grpNam)['id']
except KeyError:
	usage("Group with name '%s' doesn't exist in the source system" % grpNam)
dstGid = grp.add(dstSys, grpNam)['id']

# add members to the group
add_members(grp, srcGid, dstGid)

# copy projects from the source group to the destination one
prj = Projects()
for p in prj.by_namespace(srcSys, srcGid):
	prj.add(dstSys, p['name'], namespace_id = dstGid, **filter_dict(p, 
		'description',
		'issues_enabled',
		'merge_requests_enabled',
		'wiki_enabled',
		'snippets_enabled',
		'visibility_level'))
