'''
working with gitlab's groups
'''

from crud import Crud

class groups(Crud):
	def __init__(self):
		Crud.__init__(self, 'groups')
