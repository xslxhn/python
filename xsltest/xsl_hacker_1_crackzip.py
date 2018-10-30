#!/usr/bin/python
#--------------------------------------------------
#                       徐松亮编写
#--------------------------------------------------
import sys              # 系统
import time             # 时间
import zipfile          # 压缩与解压缩
import threading        # 多线程
#--------------------------------------------------	
StrLine = "--------------------"
LineNum = 1
time.sleep(5)
#--------------------------------------------------
#                       字典破解
#--------------------------------------------------
crackzip_str_zipfileName = "xsl_hacker_1_crackzip.zip"
crackzip_str_passfileName = "xsl_hacker_1_crackzip.txt"
#
print (StrLine,LineNum,"-字典破解解压zip文件")
LineNum+=1

zipfile_state=0
timeout=0

# fun:extract file
def extractFile(zFile, password):
    try:
        global zipfile_state 
        zFile.extractall(pwd=str.encode(password))
        print('\nFound Password = ' + password + '\n')
        zipfile_state=1
    except:
        pass
# open zip file
zfile = zipfile.ZipFile(crackzip_str_zipfileName)
# open dictionaries
passfile=open(crackzip_str_passfileName)
# read passfile line
for line in passfile.readlines():
        # strip \n
        password = line.strip('\n')
        # run thread extract file
        t = threading.Thread(target=extractFile, args=(zfile, password))
        # run thread
        t.start()
# waiting finish
while zipfile_state==0:
        timeout=timeout+1
        if timeout>10:
                break
        else:
                time.sleep(1)
# file close        
passfile.close()
zfile.close()
#--------------------------------------------------
#                       暴力破解
#--------------------------------------------------
crackzip_str_zipfile99999Name = "xsl_hacker_1_crackzip99999.zip"
#
print (StrLine,LineNum,"-暴力破解解压zip文件")
print ("5位数字暴力破解(单线程) 包括0-9 00-99 000-999 0000-9999 00000-99999")
zfile = zipfile.ZipFile(crackzip_str_zipfile99999Name)
password=0
zipfile_state=0;
ticks_begin = time.time()
zfile_cmt=0;
# fun:
def str_setlen(d,l):
        s=str(d)
        while len(s) < l:
                s='0'+s
        return s
for num in range(1,6):
        password=0
        dmax = pow(10,num)-1
        while 1:
                extractFile(zfile,str_setlen(password,num))
                password = password+1
                zfile_cmt = zfile_cmt+1
                if password>dmax or zipfile_state==1:
                        break;
                if zfile_cmt%1000==0:
                        print("%02d %%" % int((zfile_cmt*100)/(9+99+999+9999+99999)))
ticks_end = time.time()                
if zipfile_state==0:
        print ("单线程暴力破解失败 耗时(秒)=%d" % int(ticks_end-ticks_begin))
else:
        print ("单线程暴力破解成功 耗时(秒)=%d" % int(ticks_end-ticks_begin))
zfile.close()
'''
print ("5位数字暴力破解(多线程)")
zfile = zipfile.ZipFile('zip_99999.zip')
password=0
zipfile_state=0;
ticks_begin = time.time()
while(1):
        t = threading.Thread(target=extractFile, args=(zfile, str_setlen(password,5)))
        t.start()
        password = password+1
        if zipfile_state==1:
                break
while zipfile_state==0:
        if zipfile_state==1:
                break
        else:
                time.sleep(1)
ticks_end = time.time()                
if zipfile_state==0:
        print ("多线程暴力破解失败 耗时(秒)=%d" % int(ticks_end-ticks_begin))
else:
        print ("多线程暴力破解成功 耗时(秒)=%d" % int(ticks_end-ticks_begin))
zfile.close()
'''
del zfile
del passfile
del zipfile_state
del ticks_begin
del ticks_end
del zfile_cmt
#--------------------------------------------------
sys.exit()
#--------------------------------------------------

