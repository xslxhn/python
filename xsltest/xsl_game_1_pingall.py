#!/usr/bin/python

import sys              # 系统
import tkinter          # tkinter画图
import time             # 时间
import random           # 随机数
#--------------------------------------------------	
StrLine = "--------------------"
LineNum = 1
#--------------------------------------------------	
print (StrLine,LineNum,"-游戏---弹球")
LineNum+=1

class Ball:
        def __init__(self,canvas,color,paddle):
                self.canvas=canvas
                self.paddle=paddle
                # 创建小球
                self.id=canvas.create_oval(10,10,25,25,fill=color)
                # 移动小球到固定位子
                self.canvas.move(self.id,245,100)
                # 随机起始角度
                starts = [-3,-2,-1,1,2,3]
                random.shuffle(starts)
                self.x = starts[0]
                self.y = -2
                # 获取画布长宽
                self.canvas_height = self.canvas.winfo_height()
                self.canvas_width = self.canvas.winfo_width()
                # 探底变量
                self.hit_bottom=False
        def draw(self):
                # 控件移动
                self.canvas.move(self.id,self.x,self.y)
                # 根据ID获取位置
                pos = self.canvas.coords(self.id)
                # 判断上下边缘
                if pos[1] <= 0:
                        self.y = 2
                if pos[3] >= self.canvas_height:
                        self.hit_bottom=True
                if self.hit_paddle(pos) == True:
                        self.y = -2
                # 判断左右边缘
                if pos[0] <= 0:
                        self.x = 2
                if pos[2] >= self.canvas_width:
                        self.x = -2
        def hit_paddle(self,pos):
                paddle_pos = self.canvas.coords(self.paddle.id)
                if pos[2] >= paddle_pos[0] and pos[0] <= paddle_pos[2]:
                        if pos[3] >= paddle_pos[1] and pos[3] <= paddle_pos[3]:
                                return True
                return False

class Paddle:
        def __init__(self,canvas,color):
                self.canvas=canvas
                self.id=canvas.create_rectangle(0,0,100,10,fill=color)
                self.canvas.move(self.id,200,300)
                self.x=0
                self.canvas_width = self.canvas.winfo_width()
                self.canvas.bind_all('<KeyPress-Left>',self.turn_left)
                self.canvas.bind_all('<KeyPress-Right>',self.turn_right)
        def draw(self):
                # 控件移动
                self.canvas.move(self.id,self.x,0)
                # 根据ID获取位置
                pos = self.canvas.coords(self.id)
                if pos[0] <=0:
                        self.x = 0
                if pos[2] >= self.canvas_width:
                        self.x = 0
        def turn_left(self,evt):
                # 根据ID获取位置
                pos = self.canvas.coords(self.id)
                if pos[0] <= 0:
                        self.x = 0
                else:
                        self.x = -2
        def turn_right(self,evt):
                # 根据ID获取位置
                pos = self.canvas.coords(self.id)
                if pos[2] >= self.canvas_width:
                        self.x = 0
                else:
                        self.x = 2

tk=tkinter.Tk()
tk.title("Game-Ball")
# 长宽不可改变
tk.resizable(0,0)
# 窗口置前
tk.wm_attributes("-topmost",1)
# 无边框(bd=0,highlightthickness=0)
canvas = tkinter.Canvas(tk,width=500,height=400,bd=0,highlightthickness=0)
# 调整好自身大小
canvas.pack()
# 动画初始化
tk.update()

paddle=Paddle(canvas,'blue')
ball = Ball(canvas,'red',paddle)

#单独程序时，需要下面主循环，否则屏幕出现后会马上消失
while 1:
        if ball.hit_bottom==False:
                ball.draw()
                paddle.draw()
        else:
                break
        tk.update_idletasks()
        tk.update()
        time.sleep(0.01)
print ("游戏结束")
#--------------------------------------------------
sys.exit()
#--------------------------------------------------

