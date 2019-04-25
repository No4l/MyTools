# -*- coding: utf-8 -*-
#!/usr/bin/env python3
import requests
import json
import re
import os

#First,i need to get the  server response
#url = 'https://my.aliexpress.com/wishlist/wish_list_store_list_ajax.htm?callback=123456&wishstoretype=all&loadpage=1' #For Test
url = 'http://185.201.213.142:7187/'
res = requests.head(url).headers
server = res['server'] if res['server'] else ''

#Now,match the Server
for server_json in os.listdir('./plugins/server'):
    if '.json' in server_json:
        file = open('plugins/server/' + server_json)
        jsons = json.load(file)
        try:
            if re.search(jsons['response']['Server'],server).group():
                server_test = re.search(jsons['response']['Server'],server).group()
            else:
                server_test = ''
        except:
            server_test = ''
    if server_test != '':
        char = input('[*]May be '+server_test+',continue?[y/n]')
        if char == 'y':
            continue
        else:
            break

print('[*]Server '+ server_test)
# print(a['response']['Server'])
# print(re.search(a['response']['Server'],b).group())
