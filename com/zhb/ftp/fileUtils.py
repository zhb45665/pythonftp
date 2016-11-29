#!/bin/python
# -*- coding:utf-8 -*-
'''
Created on 2016年9月18日

@author: zhb
'''
from tkinter import filedialog
from tkinter import *
import ftplib
from socket import socket
from time import sleep,ctime
# from com.zhb.ftp.ftp_client import Entry_pathname_p
def selectFolder(Entry_pathname_p):
#     filename = filedialog.askopenfile("d:\py")
    filepath =  filedialog.askdirectory(initialdir = 'D:\py')
    Entry_pathname_p.set(filepath)
def connectFtp(HOST,USERNAME,PASSWD):
    try:
        ftp = ftplib.FTP(HOST)
    except (socket.error,socket.gaierror) as e:
        print("error: cannot reach %s" % HOST)
        return
    print("connected to host %s" % HOST)
    
    try:
        ftp.login(USERNAME,PASSWD)
    except (ftplib.error_perm) as f:
        print("Error: cannot login %s" % USERNAME)
        ftp.quit()
        return
    print("login as %s success" % USERNAME)
    print(ftp.getwelcome())
    return ftp
# ftp = connectFtp("10.1.253.152", "tone", "sxdxtone")
# def changePath(ftp,path):
#     ftp.cwd(path)
# #     ftp.dir()
# changePath(ftp,"/disk/disk1/rec/")
def download(ftp,loacpath,remotpath):
    try:
        ftp.retrbinary("RETR %s" % remotpath,open(loacpath,'wb').write)
        
    except ftplib.error_perm:
        print("Error: cannot read file %s " % remotpath )
    print("download success %s" % loacpath)

# download(ftp, "d:/456.txt", "list.txt")