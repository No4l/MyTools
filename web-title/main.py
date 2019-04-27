# -*- coding: utf-8 -*-
#!/usr/bin/env python3
import re
import sys
import requests
import threading
from time import sleep

heads = {
    'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_14_4) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/73.0.3683.103 Safari/537.36'
}

def checkVersion():
    PYVERSION = sys.version.split()[0]
    if PYVERSION < '3':
        exit('[-]Python3 is need.')

def exec(file):
    urls = []
    with open(file) as f:
        for i in f.readlines():
            # print(i)
            try:
                re.search('http',i).group()
                urls.append(i.strip())
            except:
                i = 'http://'+i.strip()
                urls.append(i)
    threads = []
    for i in urls:
        threads.append(threading.Thread(target=run,args=(i,False,)))

    for t in threads:
        t.setDaemon(True)
        t.start()
        sleep(0.5)

    t.join()

def run(url,bool):
    title = ''
    try:
        res = requests.get(url,timeout=1,allow_redirects=bool,headers=heads)
        status = res.status_code
    except:
        status = 0
    if status == 200:
        try:
            title = str(re.findall(b'<title>(.*)</title>',res.content)[0],encoding='utf-8')
        except:
            title = ''
    elif (status>300) and (status<400):
        run(url,True)
        exit()
    else:
        title = '5** OR 4** ERROR'
    print('[+]'+url,title,status)


if __name__ == '__main__':
    checkVersion()
    try:
        file = sys.argv[1]
    except:
        exit('[example]python main.py urlfile')
    exec(file)
