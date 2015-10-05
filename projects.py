'''
working with gitlab's projects
'''

from crud import Crud

class Projects (Crud):
	def __init__(self):
		Crud.__init__(self, 'projects', lambda x: x['path_with_namespace'])

	'''
	create a new project
	'''
	def add(self, sysNam, prjNam, **opts):
		return Crud.add(self, sysNam, dict([('name', prjNam)] + opts.items()))
