'''
working with HTTP requests & responces
'''

import config
import httplib
import urlparse

'''
make a connection to URL
'''
def mkConn(url):
	pars = urlparse.urlparse(url)
	conCls = pars.scheme == 'https' and httplib.HTTPSConnection or httplib.HTTPConnection
	return conCls(pars.netloc)

'''
send request to a system and return a response
'''
def sendReq(nam, path, meth = 'GET', body = ''):
	url = config.getURL(nam)
	cn = mkConn(url)
	cn.request(meth, '%s/api/v3/%s' % (url, path), body, {
		'PRIVATE-TOKEN': config.getToken(nam)
	})
	return cn.getresponse()
