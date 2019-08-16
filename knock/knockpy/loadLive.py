import json

datas = open('chinac_com.json').read()

jsons = json.loads(datas)

info = open('info.txt','a')
for i in jsons['subdomain_response']:
    if i['ipaddress'][0] != '61.172.243.157':
        info.write(str(i['target'])+'\n')
