#!/usr/bin/python

import sys              # 系统
import time             # 时间
import os               # 系统
import nmap             # nmap工具
#--------------------------------------------------	
StrLine = "--------------------"
LineNum = 1
#--------------------------------------------------	
print (StrLine,LineNum,"-python-nmap测试")
LineNum+=1
print ("PortScanner()：       (类)端口扫描")
print ("PortScannerAsync()：  (类)异步端口扫描")
print ("PortScannerError()：  (类)异常错误")
print ("PortScannerHostDict()：  (类)用于存储和访问主机扫描结果的特殊小类")
print ("PortScannerYield()：  (类)通过生成器使用Python中的nmap")
print ("实例: 自带测试实例，打印本地Host,测试scan是否可用")
nm = nmap.PortScanner()
nm.scan('localhost',arguments='-S 127.0.0.1')
for result in nm.all_hosts():
        print('Host : %s (%s)' % (result,nm[result].hostname()))
del nm
del result
print ("实例: 书上实例")
tgtHost='127.0.0.1'
tgtPorts=['21','22','80','8080','443','1720']
for tgtPort in tgtPorts:
        nm = nmap.PortScanner()
        nm.scan(tgtHost,tgtPort)
        state=nm[tgtHost]['tcp'][int(tgtPort)]['state']
        print (" [*] " + tgtHost + " tcp/" + tgtPort + " " + state)
del nm
print ("实例: 网上实例")
nm = nmap.PortScannerYield()
for result in nm.scan('10.32.162.61',ports='22,80,8888,8080,443',arguments="-sS"):
        print(result)
del nm
del result
#--------------------------------------------------
sys.exit()
#--------------------------------------------------

