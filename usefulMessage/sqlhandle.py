#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import pymysql

HOST = 'localhost'
USER = 'root'
PWD  = ''
DBS  = 'attackinfo'


db = pymysql.connect(HOST,USER,PWD,DBS)
cursor = db.cursor()

#搜索域名信息
def dSearch(domain):
    sql = 'select * from domains where domain="{0}"'.format(domain)
    cursor.execute(sql)
    return cursor.fetchone()

# 增加域名信息
def addDomain(domain,subdomains=[],email=[],phone=[],name=[]):
    sql = 'Insert into domains (domain,subdomain,email,phone,username) values ("%s","%s","%s","%s","%s")'%(domain,
            ','.join(subdomains),','.join(email),','.join(phone),','.join(name))
    try:
        cursor.execute(sql)
        db.commit()
        print('[+]Insert Success!')
    except:
        db.rollback()
        print('[-]Something Wrong!')

# addDomain('baidua.com',["www.baidu.com","search.baidu.com"],["test@baidu.com","admin@baidu.com"],
# ["13333333333","13888888888"],["admin","test"])
