# -*- coding: utf-8 -*-
#!/usr/bin/env python3
from cmd import Cmd
from sqlhandle import *
from webtitle import *
class MYINFO(Cmd):
    cDomain = '' # 当前选择的域名
    prompt = 'MYINFO>'
    intro  = '''Usage:
    sdomain baidu.com,GET INFO ABOUT DOMAIN
    adomain baidu.com,ADD DOMAIN INFO
    udomain baidu.com,UPDATE DOMAIN INFO
    ssdomain www.baidu.com,GET INFO ABOUT SUBDOMAIN
    asdomain test.baidu.com,ADD SUBDOMAIN INFO
    usdomain test.baidu.com,UPDATE SUBDOMAIN INFO
    use baidu.com,CHOOSE,ONE DOMAIN FOR LATER OPERATE
    webtitle,GET THE SUBDOMAIN WEBTITLE 
    show domains/subdomains,SHOW ALL DOMAINS OR ALL SUBDOMAIN ABOUT THE SELECTED DOMAIN
    help,SEE THE MESSAGE
    exit,EXIT'''

    def __init(self):
        Cmd.__init__(self)

    # 输出一个域名的详细信息，包括，子域名，邮箱，手机号
    def do_sdomain(self,arg):
        infos = dSearch(arg)
        if infos is None:
            print('[-]No Such Domain,Insert First!')
            return
        domain = infos[1]
        subDomains = self.returnInfo(infos[2])
        emails = self.returnInfo(infos[3])
        phone = self.returnInfo(infos[4])
        print('Domain:\n\t'+domain)
        print('SubDomains:')
        self.printInfo(subDomains)
        print('Emails:')
        self.printInfo(emails)
        print('Phone:')
        self.printInfo(phone)

    # 增加一个域名
    def do_adomain(self,arg):
        if dSearch(arg):
            print('[-]Domain Exists!')
            return 0

        subdomains = self.returnInfo(input('输入子域名，用逗号隔开: '))
        emails = self.returnInfo(input('输入邮箱，用逗号隔开: '))
        phones = self.returnInfo(input('输入手机号，用逗号隔开: '))
        username = self.returnInfo(input('输入用户名，用逗号隔开: '))

        addDomain(arg,subdomains,emails,phones,username)

    # 更新域名信息
    def do_udomain(self,arg):
        if not dSearch(arg):
            print('[-]Domain Not Exists!')
            return 0

        subdomains = self.returnInfo(input('输入子域名，用逗号隔开: '))
        emails = self.returnInfo(input('输入邮箱，用逗号隔开: '))
        phones = self.returnInfo(input('输入手机号，用逗号隔开: '))
        username = self.returnInfo(input('输入用户名，用逗号隔开: '))

        upDomain(arg,subdomains,emails,phones,username)

    # 输出一个子域名的详细信息
    def do_ssdomain(self,arg):
        infos = aSearch('subdomains','subdomain',arg)
        if len(infos) == 0:
            print('[-]No Such Domain,Insert First!')
            return
        infos = infos[0]
        if not len(infos):
            print('[-]No Such SubDomain!')
        else:
            print('Domain:\n\t'+str(infos[1]))
            print('Title:\n\t'+str(infos[2]))
            print('Infos:')
            self.printInfo(str(infos[4]).split('<x>'))
            print('Warn:')
            self.printInfo(str(infos[3]).split('<x>'))
            print('Vulnerability:')
            self.printInfo(str(infos[5]).split('<x>'))

    def do_asdomain(self,arg):
        if self.cDomain == '':
            print('[-]NO DOMAIN SELECTED!')
            return
        if aSearch('subdomains','subdomain',arg):
            print('[-]DOMAIN EXISTS,UPDATE PLEASE!')
            return
        webtitle = input('输入网站标题: ')
        Infos = self.returnInfo(input('输入泄漏的信息，例如robot.txt，用<x>隔开: '),tag='<x>')
        Warn = self.returnInfo(input('输入可能存在的漏洞信息，用<x>隔开: '),tag='<x>')
        Vulnerability = self.returnInfo(input('输入确认存在的漏洞信息，用<x>隔开: '),tag='<x>')
        addsDomain(subdomain=arg,domain=self.cDomain,webtitle=webtitle,
            warns=Warn,infos=Infos,error=Vulnerability)

    def do_usdomain(self,arg):
        if self.cDomain == '':
            print('[-]NO DOMAIN SELECTED!')
            return
        if not aSearch('subdomains','subdomain',arg):
            print('[-]Domain Not Exists!')
            return
        webtitle = input('输入网站标题: ')
        Infos = self.returnInfo(input('输入泄漏的信息，例如robot.txt，用<x>隔开: '),tag='<x>')
        Warn = self.returnInfo(input('输入可能存在的漏洞信息，用<x>隔开: '),tag='<x>')
        Vulnerability = self.returnInfo(input('输入确认存在的漏洞信息，用<x>隔开: '),tag='<x>')
        upsDomain(subdomain=arg,domain=self.cDomain,webtitle=webtitle,
            warns=Warn,infos=Infos,error=Vulnerability)


    def do_use(self,arg):
        domains = getAll('domains','domain')
        for domain in domains:
            if arg in domain:
                self.cDomain = arg
                print('[+]Useful domain',self.cDomain)
                return
        print('[-]Domain Not Found,Insert First.')

    def do_show(self,arg):
        flag = 0
        if arg == 'domains':
            domains = getAll('domains','domain')
        elif arg == 'subdomains':
            if self.cDomain != '':
                domains = getAll('subdomains','*','domain='+self.cDomain)
                flag = 1
            else:
                print('[-]NO DOMAIN SELECTED!')
                return
        else:
            print("[*]show domains/subdomains")
            return
        print('[+]Result:')
        for domain in domains:
            if not flag:
                print('\t'+str(domain[0]))
            else:
                print('\t'+str(domain[1]),str(domain[2]))

    def do_webtitle(self,arg):
        if self.cDomain == '':
            print('[-]NO DOMAIN SELECTED!')
            return
        domains = []
        for i in getAll('subdomains','subdomain','domain=autohome.com.cn'):
            domains.append(i[0])
        titles = webtitle(domains)
        titles.exec()


    def do_help(self,arg):
        print(self.intro)

    def returnInfo(self,info,tag=','):
        try:
            return info.split(tag)
        except:
            return [info]

    def printInfo(self,info):
        for i in info:
            if i != 'None':
                print('\t'+i)
            else:
                print()


    def do_exit(self,arg):
        return True


if __name__ == '__main__':
    myinfo = MYINFO()
    myinfo.cmdloop()
