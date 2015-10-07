'''
some utility functions
'''

'''
return a dict contains only keys from a list
'''
def filter_dict(srcDict, *leave):
	return dict(filter(lambda x: x[0] in leave, srcDict.items()))
