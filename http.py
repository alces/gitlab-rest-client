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
def mk_conn(url):
	pars = urlparse.urlparse(url)
	conCls = pars.scheme == 'https' and httplib.HTTPSConnection or httplib.HTTPConnection
	return conCls(pars.netloc)

'''
send request to a system and return a body of response
'''
def send_req(nam, path, meth = 'GET', body = '', isCorrect = lambda c: c == 200):
	url = config.get_url(nam)
	cn = mk_conn(url)
	fullUrl = '%s/api/v3/%s' % (url, path)
	cn.request(meth, fullUrl, body, {
		'PRIVATE-TOKEN': config.get_token(nam),
		'Content-Type': 'application/json'
	})
	rsp = cn.getresponse()
	ret = rsp.read()
	assert isCorrect(rsp.status), '''Server has returned an error
URL: %s
Status: %d
Body: %s''' % (fullUrl, rsp.status, ret)
	return json.loads(ret)

# send a DELETE request
delete = lambda nam, path: send_req(nam, path, 'DELETE')

# send a GET request
get = lambda nam, path: send_req(nam, path)

# send a POST request
post = lambda nam, path, hsh: send_req(nam, path, 'POST', json.dumps(hsh), lambda c: c == 201)
