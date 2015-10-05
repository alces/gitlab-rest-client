'''
working with gitlab's users
'''

from crud import Crud
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
