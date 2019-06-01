# -*- coding: utf-8 -*-
#!/usr/bin/env python
import requests
import json
import sys


BAIDU = 'http://ce.baidu.com/index/getRelatedSites?site_address='
MYSSL = 'https://myssl.com/api/v1/discover_sub_domain?domain='
CERTS = 'https://api.certspotter.com/v1/issuances?include_subdomains=true&expand=dns_names&domain='
subdomains = []

def baidu(domain):

    res = requests.get(BAIDU+domain)
    datas = json.loads(res.text)['data']
    for i in datas:
        subdomains.append(i['domain'])



def myssl(domain):
    res = requests.get(MYSSL+domain)
    datas = json.loads(res.text)['data']
    for i in datas:
        if i['domain'] in subdomains:
            subdomains.remove(i['domain'])
            subdomains.append(i['domain'])

def certs(domain):
    res = requests.get(CERTS+domain)
    datas = json.loads(res.text)
    for i in datas:
        for j in i['dns_names']:
            if j[0] != '*' and j not in subdomains:
                subdomains.append(j)


if __name__ == '__main__':
    try:
        domain = sys.argv[1]
    except:
        exit('[-]main.py domain.com')
    baidu(domain)
    myssl(domain)
    certs(domain)
    with open('domain.csv','w') as wf:
        wf.write('\n'.join(subdomains))
