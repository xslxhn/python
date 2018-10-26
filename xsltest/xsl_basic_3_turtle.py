#!/usr/bin/python

import sys              # 系统
import turtle           # 小乌龟画图
import time             # 时间
#--------------------------------------------------	
StrLine = "--------------------"
LineNum = 1
#--------------------------------------------------	
print (StrLine,LineNum,"-turtle画图")
LineNum+=1
print ("import turtle：       引用模块")
print ("turtle.Pen() ：       创建对象")
print (".forward(x)  ：       向前移动x像素")
print (".backward(x) ：       向后移动x像素")
print (".left(x)     ：       向左转动x度")
print (".right(x)    ：       向右转动x度")
print (".up()        ：       抬笔 停止作画")
print (".down()      ：       下笔 继续作画")
print (".setheading(x)：      面向指定方向")
print (".begin_fill()：       开始填充")
print (".end_fill()  ：       结束填充")
print (".circle(x)   ：       画指定大小的圆")
print (".color(r,g,b)：       设置画笔颜色(0-1)")

t1=turtle.Pen()  # 创建画布
t2=turtle.Pen()  # 创建画布
# 双点画图
print ("双点画图\n")
t2.up()
t2.left(90)
t2.forward(200) 
t2.right(90)
t2.down()

t1.forward(50)
t2.forward(50)
t1.left(90)
t2.left(90)
t1.forward(50)
t2.forward(50)   
t1.right(90)
t2.right(90)
t1.forward(50)
t2.forward(50)
t1.right(90)
t2.right(90)
t1.forward(50)
t2.forward(50)  
t1.left(90)
t2.left(90)

time.sleep(1)
t1.clear()       # 清屏但turtle位置不变
t2.clear()
time.sleep(1)
# 画两条线
print ("画平行线\n")
t1.reset()       # 清屏且turtle位置复位
t1.backward(100)
t1.up()
t1.right(90)
t1.forward(20)
t1.left(90)
t1.down()
t1.forward(100)
time.sleep(1)

def turtle_xsl_draw0(_turtle,_num,_len,_angle):
        _turtle.reset()
        for x in range(1,_num+1):
                _turtle.forward(_len)
                _turtle.left(_angle)
        return
# 画方形
print ("画方\n")
turtle_xsl_draw0(t1,4,300,90)
time.sleep(1)
# 画8角星星
print ("画8角星星\n")
turtle_xsl_draw0(t1,8,300,225)
time.sleep(1)
# 画8角星星
print ("画37角旋涡星\n")
turtle_xsl_draw0(t1,37,300,175)
time.sleep(1)
# 画8角星星
print ("画19角螺旋星\n")
turtle_xsl_draw0(t1,19,300,95)
time.sleep(1)
# 画中空星星
print ("画9角中空星\n")
t1.reset()
for x in range(1,2*9+1):
        t1.forward(200)
        if x%2==0:
                t1.left(175)
        else:
                t1.left(225)
time.sleep(1)
# 画小汽车
t1.reset()
t1.color(1,0,0)
t1.begin_fill()
t1.forward(100)
t1.left(90)
t1.forward(20)
t1.left(90)
t1.forward(20)
t1.right(90)
t1.forward(20)
t1.left(90)
t1.forward(60)
t1.left(90)
t1.forward(20)
t1.right(90)
t1.forward(20)
t1.left(90)
t1.forward(20)
t1.end_fill()

t1.color(0,0,0)
t1.up()
t1.forward(10)
t1.down()
t1.begin_fill()
t1.circle(10)
t1.end_fill()

t1.setheading(0)
t1.up()
t1.forward(90)
t1.right(90)
t1.forward(10)
t1.setheading(0)
t1.down()
t1.begin_fill()
t1.circle(10)
t1.end_fill()
#
del x
del t1
del t2
#--------------------------------------------------
sys.exit()
#--------------------------------------------------

