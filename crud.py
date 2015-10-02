'''
generic CRUD oparations for the gitlab's objects
'''

import http

class Crud():
	def __init__(self, path):
		self.path = path
		
	'''
	get an object by system's name and id
	'''
	def byId(self, sysNam, id):
		return http.get(sysNam, '%s/%d' % (self.path, id))