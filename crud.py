'''
generic CRUD oparations for the gitlab's objects
'''

import http

class Crud():
	def __init__(self, path):
		self.path = path
		self.cache = {}

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
	
	'''
	create a cache of objects
	'''
	def mkCache(self, sysNam, keyField = 'name'):
		if sysNam not in self.cache or not self.cache[sysNam]:
			self.cache[sysNam] = dict(map(lambda e: (e[keyField], e), http.get(sysNam, self.path)))
		return self.cache[sysNam]
	
	'''
	clear cache for a given system
	'''
	def clrCache(self, sysNam):
		self.cache[sysNam] = {}

	'''
	get an object by system's name and an object's name
	'''
	def byName(self, sysNam, objNam):
		return self.mkCache(sysNam)[objNam]
