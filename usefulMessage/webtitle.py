import re
import requests
import threading
from time import sleep
from sqlhandle import *
class webtitle:

    heads = {
        'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_14_4) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/73.0.3683.103 Safari/537.36'
    }

    def __init__(self,domains):
        self.domains = domains

    def exec(self):
        for i in range(len(self.domains)):
            self.domains[i] = 'http://'+self.domains[i]

        threads = []
        for i in self.domains:
            threads.append(threading.Thread(target=self.run,args=(i,)))

        for t in threads:
            t.setDaemon(True)
            t.start()

        for t in threads:
            t.join()

    def run(self,url):
        title = ''
        try:
            res = requests.get(url,timeout=1,headers=self.heads)
            status = res.status_code
        except:
            status = 0
        if status == 200:
            try:
                title = str(re.findall(b'<title>(.*)</title>',res.content)[0],encoding='utf-8')
            except:
                try:
                    title = str(re.findall(b'<title>(.*)</title>',res.content)[0],encoding='GBK')
                except:
                    title = ''
        else:
            title = ''
        print('[+]'+url,title,status)
        update('subdomains','webtitle',title,'subdomain="'+url.split('//')[1]+'"')
