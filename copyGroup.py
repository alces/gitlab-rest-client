#!/usr/bin/env python

'''
copy a group with all its members and projects from one gitlab server to another
'''

import getopt
import sys
from groups import Groups
from projects import Projects
from utils import filter_dict

def usage(msg = ''):
	mess = msg and msg or "Usage: %s -s sourceSystem -d destinationSystem -g groupName" % sys.argv[0]
	sys.stderr.write(mess + '\n')
	sys.exit(2)

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
