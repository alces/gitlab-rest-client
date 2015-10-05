'''
working with gitlab's users
'''

from crud import Crud
import random

class Users (Crud):
	def __init__(self):
		Crud.__init__(self, 'users', lambda x: x['username'])

	'''
	create a new user
	'''
	def add(self, sysNam, login, fullName, email, **opts):
		return Crud.add(self, sysNam, dict(
			[('name', fullName), ('username', login), ('email', email)]
			+ ('password' in opts and [] or [('password', ''.join(chr(random.randint(64, 122)) for x in xrange(10)))])
			+ opts.items()))
