'''
working with gitlab's groups
'''

from crud import Crud

class Groups(Crud):
	def __init__(self):
		Crud.__init__(self, 'groups')

	'''
	add a new group
	'''
	def add(self, sysNam, grpNam):
		return Crud.add(self, sysNam, {'name': grpNam, 'path': grpNam})
