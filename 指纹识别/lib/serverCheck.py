import re
import os
import json
from lib.whattodo import resCheck
from lib.whattodo import errorCheck


def serverCheck(url,res):
    server = res['server'] if res['server'] else ''
    for server_json in os.listdir('./plugins/server'):
        server_test = ''
        if '.json' in server_json:
            file = open('plugins/server/' + server_json)
            jsons = json.load(file)

            #response check
            server_test = resCheck(jsons,server)
            #error check

            if server_test == '':
                server_test = errorCheck(jsons,url)

        if server_test != '':
            char = input('[*]May be '+server_test+',continue?[y/n]')
            if char == 'y':
                continue
            else:
                break
    return server_test
