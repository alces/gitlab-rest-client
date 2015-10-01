'''
read gitlab systems' configuration
'''

import json
import os

cfgpath = os.path.join(os.environ['HOME'], '.gitlab_systems.json')

assert os.path.isfile(cfgpath), "config file %s doen't exist" % cfgpath
assert os.stat(cfgpath).st_mode & 066 == 0, '%s should be readable and writable only for its owner' % cfgpath

syscfg = json.load(open(cfgpath))

'''
get configuration for a named system
'''
def getSys(nam):
	assert nam in syscfg, "System %s doesn't exist in %s" % (nam, cfgpath)
	return syscfg[nam]

# get a system's URL
getURL = lambda x: getSys(x)['url']

# get a system's token
getToken = lambda x: getSys(x)['token']