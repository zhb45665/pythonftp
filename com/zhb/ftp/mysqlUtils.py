#!/bin/python
# -*- coding:utf-8 -*-
'''
Created on 2016年9月21日

@author: zhb
'''
import pymysql
def connect(ip,dbname):
    cxn = pymysql.connect(host=ip,port=3306,user='root',passwd='root',db=dbname,charset='utf8')
    cur = cxn.cursor()
#     cur.execute("select id,call_to,empid from shangluo")
#     for date in cur.fetchall():
#        print("%s \t %s　\t %s" % date)
#        print(date[1])
#     cur.close()
#     cxn.close()
    return cur
def closeServer(cxn):
    cxn.close()