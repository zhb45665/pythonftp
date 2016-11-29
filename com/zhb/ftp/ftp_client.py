#!/bin/python
# -*- coding:utf-8 -*-
'''
Created on 2016��9��18��

@author: zhb
'''
import sys
sys.path.append("C:/Users/zhb/workspace/win32/")
from com.zhb.ftp.mysqlUtils import *
from com.zhb.ftp.fileUtils import *
import tkinter
from tkinter import *
import os
top = tkinter.Tk()
top.title("ftp")
top.geometry("450x400")
# variable = StringVar(top)
global ftp, cur
tkinter.Label(top).grid(row=1)
# def login():
# #     print(variable_host.get())
# #     ftp = connectFtp("10.1.253.152", "tone", "sxdxtone")
#     print(variable_dbname_p.get())
#     cur = connect(variable_host.get(),variable_dbname_p.get())
#     print(Entry_pathname_p.get())
#     return ftp,cur
def downloadfile():
    print(variable_host.get())
    ftp = connectFtp("10.1.253.152", "root", "ZT@txl10")
    print(variable_dbname_p.get())
    cur = connect(variable_host.get(), variable_dbname_p.get())
    print(Entry_pathname_p.get())
    ftp.cwd("/")
    cur.execute("SELECT a.quesstion,a.phone,a.area,b.initPath,b.recPath from a_copy a,zx_rec_info_bak b where a.phone = b.call_to;")
    filelist = cur.fetchall()

    for date in filelist:
#         remote = date[2][27:84]
#         remopath = date[2][0:27]
        remote = date[4][32:53]
        remopath = "/" + (date[3] + date[4])[0:46]
        localpath = Entry_pathname_p.get()
#         localname = localpath+"/"+date[3]
        local = localpath + "/" + date[0] + "/" + date[2] + "/"
        localname = localpath + "/" + date[0] + "/" + date[2] + "/" + date[1] + ".wav"
        print(date[0])
        print(remopath)
        print(remote)
        print(localname)
        if os.path.isdir(local):
            try:
                ftp.cwd(remopath)
                download(ftp, localname, remote)
            except ftplib.error_perm:
                print("Error: cannot read file %s " % remopath)
        else:
            os.makedirs(local)
            ftp.cwd(remopath)
            download(ftp, localname, remote)
#         print("%s****%s@@@@@@%s##########%s" % date)
    ftp.close()
    cur.close()
    
label_host = tkinter.Label(top, text="HOST地址：").grid(row=2, column=0)
# Entry_host = tkinter.Entry(top).grid(row = 2,column = 2)
variable_host = StringVar()
variable_host.set("10.1.250.56")
# iteam = ["10.1.250.56", "10.1.250.54", "10.1.250.59"]
OptionMenu(top, variable_host, "10.1.250.56", "10.1.250.54", "10.1.250.59").grid(row=2, column=2)
tkinter.Label(top).grid(row=3)
print(variable_host.get())
label_tablename = tkinter.Label(top, text="表名字：").grid(row=4, column=0)
Entry_tablename_p = StringVar()
Entry_tablename = tkinter.Entry(top, textvariable=Entry_tablename_p).grid(row=4, column=2)
tkinter.Label(top).grid(row=5)

label_dbname = tkinter.Label(top, text="数据库名：").grid(row=6, column=0)
variable_dbname_p = StringVar()
variable_dbname_p.set("zxin_customers_visit_mining_policy")
OptionMenu(top, variable_dbname_p, "zxin_haosenwei", "customers_visit_business_upgrade", "zxin_customers_visit_mining_policy", "pingan_record").grid(row=6, column=2)
# Entry_dbname = tkinter.Entry(top,textvariable=Entry_dbname_p).grid(row = 6,column = 2)

tkinter.Label(top).grid(row=7)
label_pathname = tkinter.Label(top, text="本地路径：").grid(row=8, column=0)

Entry_pathname_p = StringVar()
Entry_pathname = tkinter.Entry(top, textvariable=Entry_pathname_p,).grid(row=8, column=2)
Button_pathname = tkinter.Button(top, text="选择", command=lambda:selectFolder(Entry_pathname_p), default='active').grid(row=8, column=3)


tkinter.Label(top).grid(row=9)
Button_login = tkinter.Button(top, text="登陆").grid(row=10, column=1)
Button_download = tkinter.Button(top,text="下载", command=downloadfile).grid(row=10, column=2)

tkinter.Label(top).grid(row=11)
# variable = StringVar(top)
# variable.set("中文") # default value
# OptionMenu(top, variable, "中文", "英文", "日文").grid(row = 13,column = 2)

Text_info = tkinter.Text(top, height=10, width=42)
Text_info.grid(row=14, column=0, columnspan=4)

tkinter.mainloop()
