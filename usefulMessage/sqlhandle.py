#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import pymysql

HOST = 'localhost'
USER = 'root'
PWD  = ''
DBS  = 'attackinfo'




#搜索域名信息
def dSearch(domain):
    db = pymysql.connect(HOST,USER,PWD,DBS)
    cursor = db.cursor()
    sql = 'select * from domains where domain="{0}"'.format(domain)
    cursor.execute(sql)
    return cursor.fetchone()

# 搜索信息
def aSearch(table,column,value):
    db = pymysql.connect(HOST,USER,PWD,DBS)
    cursor = db.cursor()
    sql = 'select * from {0} where {1}="{2}"'.format(table,column,value)
    cursor.execute(sql)
    return cursor.fetchall()

# 增加域名信息
def addDomain(domain,subdomains=set([]),email=([]),phone=([]),name=([])):
    db = pymysql.connect(HOST,USER,PWD,DBS)
    cursor = db.cursor()
    sql = 'Insert into domains (domain,subdomain,email,phone,username) values ("%s","%s","%s","%s","%s")'%(domain,
            ','.join(subdomains),','.join(email),','.join(phone),','.join(name))
    try:
        cursor.execute(sql)
        db.commit()
        sql = 'Insert into subdomains (subdomain,domain) values'
        for subdomain in subdomains:
            if subdomain.find('http'):
                subdomain = subdomain.replace('http://','').replace('https://','')
            sql += '("%s","%s"),'%(subdomain,domain)
        try:
            cursor.execute(sql[:-1])
            db.commit()
            print('[+]Insert Success!')
        except:
            db.rollback()
            print('[-]Insert Into subDomains Wrong!')
    except:
        db.rollback()
        print('[-]Insert Into Domains Wrong!')

# 更新域名信息
def upDomain(domain,subdomains=[],email=[],phone=[],name=[]):
    db = pymysql.connect(HOST,USER,PWD,DBS)
    cursor = db.cursor()
    sql = 'update domains set subdomain="%s",email="%s",phone="%s",username="%s" where domain="%s"'%(','.join(subdomains),
    ','.join(email),','.join(phone),','.join(name),domain)

    try:
        cursor.execute(sql)
        db.commit()
        try:
            flag = 0
            for subdomain in subdomains:
                if subdomain.find('http'):
                    subdomain = subdomain.replace('http://','').replace('https://','')
                if not checkExist('subdomains','subdomain',subdomain):
                    if not flag:
                        sql = 'Insert into subdomains (subdomain,domain) values'
                        flag = 1
                    sql += '("%s","%s"),'%(subdomain,domain)
            if flag:
                cursor.execute(sql[:-1])
                db.commit()
            print('[+]Update Success!')
        except:
            db.rollback()
            print('[-]Update SubDomain Wrong!')
    except:
        db.rollback()
        print('[-]Update Domain Wrong!')

# 增加子域名信息
def addsDomain(subdomain,domain,webtitle='',warns=([]),infos=([]),error=([])):
    db = pymysql.connect(HOST,USER,PWD,DBS)
    cursor = db.cursor()
    sql = 'Insert into subdomains (subdomain,webtitle,warns,infos,error,domain) values ("%s","%s","%s","%s","%s","%s")'%(subdomain,
            webtitle,'<x>'.join(warns),'<x>'.join(infos),'<x>'.join(error),domain)
    try:
        cursor.execute(sql)
        db.commit()
        print('[+]Insert Success!')
    except:
        db.rollback()
        print('[-]Insert Into SubDomains Wrong!')

# 更新子域名信息
def upsDomain(subdomain,domain,webtitle='',warns=([]),infos=([]),error=([])):
    db = pymysql.connect(HOST,USER,PWD,DBS)
    cursor = db.cursor()
    sql = 'Update subdomains set domain="%s",webtitle="%s",warns="%s",infos="%s",error="%s" where subdomain="%s"'%(domain,
            webtitle,'<x>'.join(warns),'<x>'.join(infos),'<x>'.join(error),subdomain)
    try:
        cursor.execute(sql)
        db.commit()
        print('[+]Update Success!')
    except:
        db.rollback()
        print('[-]Update SubDomains Wrong!')

# 获取某个表某一列所有信息
def getAll(table,column,where=''):
    db = pymysql.connect(HOST,USER,PWD,DBS)
    cursor = db.cursor()
    sql = 'select %s from %s' % (column,table)
    if where != '':
        exp = where.split('=')
        sql += ' where ' + exp[0] + ' = "%s"'%exp[1]
    cursor.execute(sql)
    return cursor.fetchall()


# 更新某样信息
def update(table,column,value,where):
    db = pymysql.connect(HOST,USER,PWD,DBS)
    cursor = db.cursor()
    sql = 'update %s set %s="%s" where %s'%(table,column,value,where)
    try:
        cursor.execute(sql)
        db.commit()
    except:
        db.rollback()
        print('[-]Update %s for %s  at %s Wrong!'%(value,column,where))



# 判断信息是否存在
def checkExist(table,column,value):
    db = pymysql.connect(HOST,USER,PWD,DBS)
    cursor = db.cursor()
    sql = 'select * from %s where %s="%s"'%(table,column,value)
    cursor.execute(sql)
    if cursor.fetchone():
        return 1
    else:
        return 0
