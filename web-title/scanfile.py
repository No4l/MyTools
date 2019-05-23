# -*- coding: utf-8 -*-
#!/usr/bin/env python3
import re
import requests
import threading
from queue import Queue

heads = {
    'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_14_4) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/73.0.3683.103 Safari/537.36'
}

q = Queue()
files = [] # 200
forbidden = [] # 403
nothing = [] # 200 but no content
everything = [] # 200 but error
def exec():
    urls = set({})
    with open('domain.txt') as f:
        for i in f.readlines():
            if 'http' in i:
                urls.add(i.strip()+'/')
            else:
                urls.add('http://'+i.strip()+'/')

    for i in urls:
        urls = urls | scanFile(i)
    for i in urls:
        q.put(i)
    threads = []
    for i in range(100):
        threads.append(threading.Thread(target=run,args=(q,False,)))

    for t in threads:
        t.setDaemon(True)
        t.start()

    for t in threads:
        t.join()
# 隐私文件
def scanFile(url):
    flag = 0
    backs = set({})
    results = set({})
    url = url.replace('http://','')
    domain = url.split('.')
    with open('back.txt') as f:
        for i in f.readlines():
            backs.add(i.strip())
    for i in domain[:-1]:
        for j in backs:
            if '?' in j:
                j = j.replace('?',i)
            try:
                # res = requests.get('http://'+url+'/'+j,timeout=1)
                # if res.status_code == 200:
                #     flag += 1
                results.add('http://'+url+'/'+j)
            except:
                continue
    return results

def run(q,bool):
    while not q.empty():
        url = q.get()
        flag = 0
        text = ''
        try:
            res = requests.get(url,timeout=1,allow_redirects=bool,headers=heads)
            status = res.status_code
            text = res.text
            length = len(text)
        except:
            status = 0

        title = re.search('<title>.*?</title>',text)

        try:
            title.group()
            flag = 1
        except:
            flag = 0

        if status == 403 or status == 200:
            if status == 200:
                if flag:
                    everything.append(url)
                elif length == 0:
                    nothing.append(url)
                else:
                    files.append(url+' length: '+str(length))
            else:
                forbidden.append(url)
            print('[%s]'%status,url,'length:',length)


if __name__ == '__main__':
    f = open('log.txt','w')
    f.write('status,url')
    f.close()
    exec()
    wf = open('log.txt','a')
    wf.write('\nFILES:\n\t'+'\n\t'.join(files))
    wf.write('\n\n\n\tNothing:\n\t\t'+'\n\t\t'.join(nothing))
    wf.write('\n\n\n\tEverything:\n\t\t'+'\n\t\t'.join(everything))
    wf.write('\n\n\nForbidden:\n\t'+'\n\t'.join(forbidden))
