#!/usr/bin/python

import sys              # 系统
import tkinter          # tkinter画图
import time             # 时间
import random           # 随机数

from xsl_basic_2_tkinter_CanvasDemo import CanvasDemo
#--------------------------------------------------	
StrLine = "--------------------"
LineNum = 1
#--------------------------------------------------	
print (StrLine,LineNum,"-tkinter画图")
LineNum+=1
print (".Tk          ：       创建对象")
print (".Button      ：       创建按钮")
print (".Canvas      ：       创建画布")
# 按钮回调函数
def tkinter_fun0():
	print ("tkinter_fun0")
	return
# 画随机矩形
def tkinter_fun1(width,height):
        x1 = random.randrange(width)
        y1 = random.randrange(height)
        x2 = x1 + random.randrange(width)
        y2 = y1 + random.randrange(height)
        canvas.create_rectangle(x1,y1,x2,y2)
        return
tk=tkinter.Tk()
print ("画按钮")
btn=tkinter.Button(tk,text="click me",command=tkinter_fun0)
btn.pack()
print ("创建画布")
canvas = tkinter.Canvas(tk,width=500,height=500)
canvas.pack()
print ("画布->画线")
canvas.create_line(0,0,500,500)
print ("画布->画长方形")
for x in range(0,50):
        tkinter_fun1(500,500)
print ("画布->填充长方形")
canvas.create_rectangle(10,10,20,40,fill='#ffd800')
time.sleep(1)
canvas.delete("rect","oval","arc","polygon","line","string")
print ("运行画布Demo")
canvas_demo=CanvasDemo()
del tk
del btn
del canvas
del x
#--------------------------------------------------
sys.exit()
#--------------------------------------------------

