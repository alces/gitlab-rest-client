'''
working with gitlab's users
'''

from crud import Crud
from utils import filter_dict
import random

class Users (Crud):	
	def __init__(self):
		Crud.__init__(self, 'users', lambda x: x['username'])

	# generate random password
	rand_pass = lambda s, l = 10: ''.join(chr(random.randint(64, 122)) for x in xrange(l))

	'''
	create a new user
	'''
	def add(self, sysNam, login, fullName, email, **opts):
		return Crud.add(self, sysNam, dict(
			[('name', fullName), ('username', login), ('email', email)]
			+ ('password' in opts and [] or [('password', self.rand_pass())])
			+ opts.items()))

# for saving users' cache between the calls of get_user()
_usrs = Users()

'''
if a user represented by usrDict is found in the system, then return its id
else - create a new one and return its id
'''
def get_user(sysNam, usrDict):
	try:
		usr = _usrs.by_name(sysNam, usrDict['username'])
	except KeyError:
		# add the 1st identity to a users' dict
		dictWithUuid = filter_dict(dict(usrDict.items() + (usrDict['identities'] and usrDict['identities'][0].items() or [])),
			'admin',
			'bio',
			'can_create_group',
			'extern_uid',
			'linkedin',
			'password',
			'projects_limit',
			'provider',
			'skype',
			'twitter',
			'website_url')
		usr = _usrs.add(sysNam, usrDict['username'], usrDict['name'], usrDict['email'], confirm = False, **dictWithUuid)
		# rebuilding of cache after adding a new user is needed
		_usrs.clr_cache(sysNam)
	return usr['id']

