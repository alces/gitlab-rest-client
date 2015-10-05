'''
working with gitlab's projects
'''

from crud import Crud
import http
import members

class Projects (Crud, members.Members):
	def __init__(self):
		Crud.__init__(self, 'projects', lambda x: x['path_with_namespace'])

	'''
	create a new project
	'''
	def add(self, sysNam, prjNam, **opts):
		return Crud.add(self, sysNam, dict([('name', prjNam)] + opts.items()))
	
	'''
	get a list of branches
	'''
	def get_branches(self, sysNam, prjId):
		return http.get(sysNam, '%s/%d/repository/branches' % (self.path, prjId))

	'''
	protect/unprotect a branch
	'''
	def put_branch(self, sysNam, prjId, brNam, cmd):
		return http.put(sysNam, '%s/%d/repository/branches/%s/%s' % (self.path, prjId, brNam, cmd),
			{'id': prjId, 'branch': brNam})
	
	# shortcut for protect a branch
	protect = lambda self, sn, pr, br: self.put_branch(sn, pr, br, 'protect')
	
	# shortcut for unprotect a branch
	unprotect = lambda self, sn, pr, br: self.put_branch(sn, pr, br, 'unprotect')
