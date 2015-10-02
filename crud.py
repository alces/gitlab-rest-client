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

	'''
	add a new instance of an object
	'''
	def add(self, sysNam, data):
		return http.post(sysNam, self.path, data)

	'''
	delete an instcnce by id
	'''
	def delete(self, sysNam, id):
		return http.delete(sysNam, '%s/%d' % (self.path, id))

