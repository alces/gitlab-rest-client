#!/usr/bin/env python

'''
copy a group with all its members and projects from one gitlab server to another
'''

import getopt
import sys
from groups import Groups

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
	
grp = Groups()
try:
	srcGid = grp.by_name(srcSys, grpNam)['id']
except KeyError:
	usage("Group with name '%s' doesn't exist in the source system" % grpNam)

grp.add(dstSys, grpNam)
