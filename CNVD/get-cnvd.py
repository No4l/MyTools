# -*- coding: utf-8 -*-
#!/usr/bin/env python3
import argparse
import requests
import redis
import json
import sys
import re
import os

#import user info
try:
    UserInfo = json.load(open('userinfo.json'))
except:
    print('[-]Load Json File Error!')
    exit()

#use redis
r = redis.Redis(host=UserInfo['Host'],port=UserInfo['Port'],password=UserInfo['Pwd'])
try:
    acount = r.scard('CNVD')
    print('[+]目前漏洞数为:',acount)
except Exception as e:
    print('[-]Redis',e)
    exit()

def scanCNVD():
    res = requests.post(UserInfo['Url'],data=UserInfo['Data'],headers=UserInfo['Headers'])
    text = bytes.decode(res.content)
    infos = re.findall('</img> <a\s.+href="/flaw/show/(.*?)"?\s+title="(.*?)">',text)
    for i in infos:
        info = i[0]+','+i[1]
        if r.sadd('CNVD',info):
            print('[*]New Info:',info)
    print('[*]Scan Finish.')
    r.save()

def writeFile():
    cont = [bytes.decode(i) for i in r.smembers('CNVD')]
    if os.path.isfile('CNVD.csv'):
        with open('CNVD.csv','a') as af:
            af.write('\n'.join(cont))
    else:
        with open('CNVD.csv','w') as wf:
            wf.write('编号,内容\n'+'\n'.join(cont))
    print('[+]Save In CNVD.csv.')

if __name__ == '__main__':
    parse = argparse.ArgumentParser(description="CNVD INFO.")
    parse.add_argument('--update','-u',action='store_true',help='Update CNVD INFO')
    parse.add_argument('--file','-f',action='store_true',help='Save CNVD INFO')
    args = parse.parse_args()
    try:
        sys.argv[1]
    except:
        parse.print_help()
        exit()
    if args.file:
        writeFile()
    if args.update:
        scanCNVD()
