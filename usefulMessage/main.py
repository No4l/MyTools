# -*- coding: utf-8 -*-
#!/usr/bin/env python3
from cmd import Cmd
from sqlhandle import *

class MYINFO(Cmd):
    prompt = 'MYINFO>'
    intro  = '''\n\nUsage:
    dsearch domain GET INFO ABOUT DOMAIN
    adomain domain ADD DOMAIN INFO
    help SEE THE MESSAGE
    exit EXIT\n\n'''

    def __init(self):
        Cmd.__init__(self)

    def do_dsearch(self,arg):
        infos = dSearch(arg)
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

    def do_adomain(self,domain):
        if dSearch(domain):
            print('[-]Domain Exists!')
            return 0
        subdomains = self.returnInfo(input('输入子域名，用逗号隔开: '))
        emails = self.returnInfo(input('输入邮箱，用逗号隔开: '))
        phones = self.returnInfo(input('输入手机号，用逗号隔开: '))
        username = self.returnInfo(input('输入用户名，用逗号隔开: '))
        addDomain(domain,subdomains,emails,phones,username)

    def do_help(self,arg):
        print(self.intro)

    def returnInfo(self,info):
        try:
            return info.split(',')
        except:
            return [info]

    def printInfo(self,info):
        for i in info:
            print('\t'+i)

    def do_exit(self,arg):
        return True


if __name__ == '__main__':
    myinfo = MYINFO()
    myinfo.cmdloop()
