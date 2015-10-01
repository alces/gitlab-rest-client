'''
working with HTTP requests & responces
'''

import config
import httplib
import json
import urlparse

'''
make a connection to URL
'''
def mkConn(url):
	pars = urlparse.urlparse(url)
	conCls = pars.scheme == 'https' and httplib.HTTPSConnection or httplib.HTTPConnection
	return conCls(pars.netloc)

'''
send request to a system and return a body of response
'''
def sendReq(nam, path, meth = 'GET', body = '', isCorrect = lambda c: c == 200):
	url = config.getURL(nam)
	cn = mkConn(url)
	cn.request(meth, '%s/api/v3/%s' % (url, path), body, {
		'PRIVATE-TOKEN': config.getToken(nam),
		'Content-Type': 'application/json'
	})
	rsp = cn.getresponse()
	ret = rsp.read()
	assert isCorrect(rsp.status), '''Server has returned an error
URL: %s
Status: %d
Body: %s
''' % (url, rsp.status, ret)
	return json.loads(ret)

# send a DELETE request
delete = lambda nam, path: sendReq(nam, path, 'DELETE')

# send a GET request
get = lambda nam, path: sendReq(nam, path)

# send a POST request
post = lambda nam, path, hsh: sendReq(nam, path, 'POST', json.dumps(hsh), lambda c: c == 201)
