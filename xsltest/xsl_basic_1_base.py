#!/usr/bin/python

'''
这是多行注释
'''

"""
这也是多行注释
"""
StrLine = "--------------------"
LineNum = 1
#--------------------------------------------------
import keyword          # 关键字
import random           # 随机数
#import turtle           # 小乌龟画图
import sys              # 系统
import time             # 时间
import pickle           # pickle“腌菜”保存模块
#import tkinter          # tkinter画图
#import zipfile          # 压缩与解压缩
import threading        # 多线程
import os               # 系统
#import nmap             # nmap工具
import platform         # 平台信息
# 线程
#from threading import Thread
# xsl
#--------------------------------------------------
print (StrLine,LineNum,"-将信息输出到指定文件，并在控制台打印")
class Logger(object):
    def __init__(self, fileN="xsl_basic_1_base_log.txt"):
        self.terminal = sys.stdout
        self.log = open(fileN, "w")
 
    def write(self, message):
        self.terminal.write(message)
        self.log.write(message)
        # 更新内容到磁盘，否则只是到缓存
        self.log.flush()
 
    def flush(self):
        pass
sys.stdout = Logger("xsl_basic_1_base_log.txt")
#--------------------------------------------------
print (StrLine,LineNum,"-待解决问题")
LineNum+=1
print ("* logging类的应用")
print ("* 沉默获取管理员权限")
print ("* 彻底删除文件，包括删除自己")
print ("* 文件内容加密与解密")
print ("* 向服务器传送文件")
#--------------------------------------------------
print (StrLine,LineNum,"-零散知识点")
LineNum+=1
print ("* 类似C语言中的sprintf: 直接用%即可,例如：str1='%02x %02d' % (i,j)")
#--------------------------------------------------
print (StrLine,LineNum,"-查看系统信息")
LineNum+=1
print (sys.version)
print ("platform.architecture():   " , platform.architecture())
print ("platform.system():         " , platform.system())
print ("platform.version():        " , platform.version())
print ("platform.machine():        " , platform.machine())
print ("platform.python_version(): " , platform.python_version())
#--------------------------------------------------

#--------------------------------------------------
# 基本操作: 数据类型类型(数字，字符串，列表，元组，字典)
"""
数字
                int		有符号整数
                long		长整形
                float	        浮点型
                complex	        复数
字符串          string
                1,单行可以用单引号'-'，也可以用双引号"-".
                2,多行要用'''-'''
                3,支持转义字符'\',
                4,支持乘法，常用于打印一定数量(但不能用减法与除法)
列表            list
                1,相当于C语言中的数组，但python有一些方法可以实现添加删除等操作
                2,.append()       -->     追加
                3,del             -->     删除整个列表或指定元素
                4,支持乘法，常用于打印一定数量(但不能用减法与除法)
                
元祖(只读)      tuple
                1,使用括号的列表,与列表的区别在于"只读"
字典            map
                1,与列表的区别在于每个元素都有键值
"""
print (StrLine,LineNum,"-数据类型")
LineNum+=1
counter = 100  # 整型变量
print ("打印整型变量  ：",counter)
print ("类似于C中的printf：counter = %d" % (counter))
del counter
miles = 1000.0 # 浮点型
print ("打印浮点变量  ：",miles)
del miles
name = "XSL"   # 字符串    
print ("打印字符串乘法：",name)
name = name*10
print ("打印字符串    ：",name)
del name
listname = ['item1', 'item2', 'item3'];
print ("打印列表      ：",listname)
listname.append('append')
print ("打印列表(追加)：",listname)
del listname[2]
print ("打印列表(追加)：",listname)
del listname
tuple = ( 'runoob', 786 , 2.23, 'john', 70.2 );
print ("打印元祖      ：",tuple)
del tuple
dict = {}
dict['one']="this is one"
dict[2]="This is two"
tinydict={'name':'xsl','code':824}
print ("打印字典(成员)：",dict['one'],dict[2])
print ("打印字典(整体)：",tinydict)
print ("打印字典(键值)：",tinydict.keys())
print ("打印字典(值  )：",tinydict.values())
del tinydict
#--------------------------------------------------
print (StrLine,LineNum,"-内建函数")
LineNum+=1
print ("-----------Number类型转")
print ("int(x[,base])         将x转换为一个整数")
print ("long(x[,base])        将x转换为一个长整数")
print ("float(x)              将x转换为一个浮点数")
print ("complex(real[,imag])  创建一个复数")
print ("str(x)                将对象x转换为字符串")
print ("repr(x)               将对象x转换为表达式字符串")
print ("eval(str)             用来计算在字符串中的有效Python表达式，并返回一个对象")
print ("tuple(s)              将序列 s 转换为一个元组")
print ("list(s)               将序列 s 转换为一个列表")
print ("chr(x)                将一个整数转换为一个字符")
print ("unichr(x)             将一个整数转换为Unicode字符")
print ("ord(x)                将一个字符转换为它的整数值")
print ("hex(x)                将一个整数转换为一个十六进制字符串")
print ("oct(x)                将一个整数转换为一个八进制字符串")
print ("bool(x)               将一个参数转为布尔类型 0/空-False 非0/非空-True")
print ("-----------数学函数")
print ("abs(x)                返回数字的绝对值，如abs(-10) 返回 10")
print ("ceil(x)               返回数字的上入整数，如math.ceil(4.1) 返回 5")
print ("cmp(x, y)             如果 x < y 返回 -1, 如果 x == y 返回 0, 如果 x > y 返回 1")
print ("exp(x)                返回e的x次幂(ex),如math.exp(1) 返回2.718281828459045")
print ("fabs(x)               返回数字的绝对值，如math.fabs(-10) 返回10.0")
print ("floor(x)              返回数字的下舍整数，如math.floor(4.9)返回 4")
print ("log(x)                如math.log(math.e)返回1.0,math.log(100,10)返回2.0")
print ("log10(x)              返回以10为基数的x的对数，如math.log10(100)返回 2.0")
print ("max(x1, x2,...)       返回给定参数的最大值，参数可以为序列")
print ("min(x1, x2,...)       返回给定参数的最小值，参数可以为序列")
print ("modf(x)               返回x的整数部分与小数部分，两部分的数值符号与x相同，整数部分以浮点型表示")
print ("pow(x, y)             x**y 运算后的值")
print ("round(x [,n])         返回浮点数x的四舍五入值，如给出n值，则代表舍入到小数点后的位数")
print ("sqrt(x)               返回数字x的平方根，数字可以为负数，返回类型为实数，如math.sqrt(4)返回 2+0j")
print ("-----------随机数函数")
print ("random.choice(seq)    从序列的元素中随机挑选一个元素，比如random.choice(range(10))，从0到9中随机挑选一个整数。")
print ("random.randrange ([start,] stop [,step])从指定范围内，按指定基数递增的集合中获取一个随机数，基数缺省值为1")
print ("random.random()       随机生成下一个实数，它在[0,1)范围内")
print ("random.randint(min,max)  随机生成下一个一定范围内的整数")
print ("random.seed([x])      改变随机数生成器的种子seed。如果你不了解其原理，你不必特别去设定seed，Python会帮你选择seed")
print ("random.shuffle(lst)   将序列的所有元素随机排序")
print ("random.uniform(x, y)  随机生成下一个实数，它在[x,y]范围内")
print ("-----------三角函数")
print ("acos(x)               返回x的反余弦弧度值")
print ("asin(x)               返回x的反正弦弧度值")
print ("atan(x)               返回x的反正切弧度值")
print ("atan2(y, x)           返回给定的 X 及 Y 坐标值的反正切值")
print ("cos(x)                返回x的弧度的余弦值")
print ("hypot(x, y)           返回欧几里德范数 sqrt(x*x + y*y)")
print ("sin(x)                返回的x弧度的正弦值")
print ("tan(x)                返回x弧度的正切值")
print ("degrees(x)            将弧度转换为角度,如degrees(math.pi/2) ， 返回90.0")
print ("radians(x)            将角度转换为弧度")
print ("-----------数学常量")
print ("pi                    圆周率，一般以π来表示")
print ("e                     自然常数")
print ("-----------所有关键字")
print (keyword.kwlist)
print ("-----------其他")
print ("len(s)                返回一个对象的长度")
print ("set(s)                转换为可变集合")
print ("dict(d)               创建一个字典。d 必须是一个序列 (key,value)元组。")
print ("frozenset(s)          转换为不可变集合")
#--------------------------------------------------
print (StrLine,LineNum,"-运算符")
LineNum+=1
print ("算数运算符：          + ,- ,* ,/ ,% ,**,//")
print ("比较运算符：          ==,!=,<>,> ,< ,>=,<=")
print ("赋值运算符：          = ,+=,-=,*=,/=,%=,**=,//=")
print ("按位运算符：          & ,| ,^ ,- ,<< ,>>")
print ("逻辑运算符：          and ,or ,not")
print ("成员运算符：          in ,not in")
print ("身份运算符：          is ,is not")
print ("字符串运算符：        +,*,[],[:],in,not in,r/R,%")
print ("字符串格式化运算符：  %c,%s,%d,%u,%o,%x,%X,%f,%e,%E,%g,%G,%p")
print ("  格式化运算符辅助：  *,-,+,<sp>,#,0,%,(var),m.n")
print ("字符串复杂引用：      '''")
#--------------------------------------------------
print (StrLine,LineNum,"-条件")
LineNum+=1
print ("条件语句：            if-elif-else")
num = 5
if num==1:
	print ("条件实例：if",num)
elif num==2:
	print ("条件实例：elif",num)
else:
	print ("条件实例：else")
del num
#--------------------------------------------------
print (StrLine,LineNum,"-循环")
LineNum+=1	
print ("循环语句：            while,for")
print ("循环控制语句：        break,continue,pass")
for x in range(0,2):
        print('for 实例 hello %s' % x)
del x
#--------------------------------------------------
print (StrLine,LineNum,"-打印")
LineNum+=1
# 数组赋值
for x in range(0,10):
	print (x,end = '') 
print ('')
del x
#--------------------------------------------------	
print (StrLine,LineNum,"-时间")
LineNum+=1

ticks = time.time()
print ("Unix时间戳   ：       ",ticks)
localtime = time.localtime(ticks)
print (".localtime   ：       ",localtime)
print (".asctime     ：       ",time.asctime())
print ("延时(秒)：            time.sleep(x)")
del ticks
#--------------------------------------------------	
print (StrLine,LineNum,"-文件")
LineNum+=1
text1="1234567890"
fo = open("xsl_basic_1_base.txt","w+")
fo.write(text1)
print ("创建xsl_basic_1_base.txt并写入字符串:",text1)
position=fo.tell();
print ("当前文件位置",position)
position = fo.seek(5,0)
str1=fo.read(5)
print ("定位到5,读取5字节数据:",str1)
fo.close();
#--------------------------------------------------
'''
print (StrLine,LineNum,"-文件读写---常规")
LineNum+=1
i=0
fi = open("xsl_basic_1_base_ascii.bin","rb")
fo = open("xsl_basic_1_base_asciiOut.bin","w+")
try:
	while True:
		i1=fi.read(1)
		i2=fi.read(1)

		print ("i1=",i1)
		print ("i2=",i2)
		
		if not i1:
			break;
		#i1=i1+1
		#i2=i2+1
		fo.write(str(i)+"\r\n")
finally:
	fi.close()
	fo.close()
del i
del fi
del fo
'''
#--------------------------------------------------	
print (StrLine,LineNum,"-文件读写---pickle保存模块")
LineNum+=1
save_data={'name':'pickle_name','pickle_age':36}
save_file=open('xsl_basic_1_base_pickle.dat','wb')
pickle.dump(save_data,save_file)
save_file.close()
print(".dump:",save_data)
del save_data
del save_file
loat_file=open('xsl_basic_1_base_pickle.dat','rb')
loat_data=pickle.load(loat_file)
loat_file.close()
print(".loat:",loat_data)
del loat_data
del loat_file
#--------------------------------------------------	
print (StrLine,LineNum,"-函数使用")
LineNum+=1
def xslfun(str):
	print (str)
	return
xslfun("正在调用一个函数！")
LineNum+=1
print (StrLine,'end')
#--------------------------------------------------	
print (StrLine,LineNum,"-类的使用")
LineNum+=1
#--------------------------------------------------	
print (StrLine,LineNum,"-模块的使用(模块就是函数/类/变量的组合)")
LineNum+=1
print ("turtle       ：       小乌龟画图")
print ("copy.copy    ：       浅拷贝,改变原对象影响新对象")
print ("copy.deepcopy：       深拷贝,改变原对象不影响新对象")
print ("keyword      ：       关键字")
#--------------------------------------------------	
print (StrLine,LineNum,"-输入输出")
LineNum+=1
# 输入
key=input("\n请输入按键后按回车键退出(input)\n")
print (key)
print("\n请输入按键后按回车键退出(sys.stdin.readline(max))")
key=sys.stdin.readline(5)
print (key)
del key
# 输出
print ("输出0-9 (sys.stdout.write)")
sys.stdout.write("0123456789\n")
#--------------------------------------------------耗时前退出test
print (StrLine)
print ("xsl控制系统无错退出")
os._exit(0)
#--------------------------------------------------
sys.exit()
#--------------------------------------------------

