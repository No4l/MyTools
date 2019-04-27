import re
import requests


def resCheck(jsons,server):
    try:
        if re.search(jsons['response']['Server'],server).group():
            server_test = re.search(jsons['response']['Server'],server).group()
        else:
            server_test = ''
    except:
        server_test = ''
    return server_test


def errorCheck(jsons,url):
    try:#timeout
        text = requests.get(url+'/error_test',timeout=1).text
        try:
            server_test = re.search(jsons['error']['404'],text).group()
        except:
            server_test = ''
    except:
        server_test = ''
    return server_test
