'''
Methods for working with members (inherited by groups and projects)
'''

import http

class Members():
	'''
	getting a list of members
	'''
	def get_members(self, sysNam, objId):
		return http.get(sysNam, '%s/%d/members' % (self.path, objId))

	'''
	delete a member
	'''
	def del_member(self, sysNam, objId, userId):
		return http.delete(sysNam, '%s/%d/members/%d' % (self.path, objId, userId))

	'''
	add a new member
	'''
	def add_member(self, sysNam, objId, userId, accLevel = 10):
		return http.post(sysNam, '%s/%d/members' % (self.path, objId),
			{'id': objId, 'user_id': userId, 'access_level': accLevel})
