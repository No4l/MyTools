# -*- coding: utf-8 -*-
#!/usr/bin/env python3
from lib.serverCheck import serverCheck
from utils import check
import requests
import json
import sys
import re

if __name__ == '__main__':
    url = sys.argv[1]
    try:
        re.search('http',url).group()
    except:
        url = 'http://'+url
    res = requests.head(url).headers
    server_test = serverCheck(url,res)
    print('[*]Server '+ server_test)
