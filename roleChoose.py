from tkinter import *
from tkinter import scrolledtext
import tkinter as tk
from tkinter import ttk
from PIL import ImageTk, Image
import random, sys
from tkinter.simpledialog import askinteger


def randomWord():
    fo=open("wd.txt","r",encoding='utf-8-sig')
    while True:
        line=fo.read()
        if not line:break
        a=line.replace('；',' ')
        a=a.strip().split( )
        num=len(a)
    spy=random.randint(0,num-1)
    b=a[spy].replace('-',' ')
    b=b.split( )
    return b
    fo.close()

def checkPlayerNum(t):
    if t<4 or t>8:
        tk.messagebox.showerror('错误','输入人数限制在4~8人\n请您输入正确人数,重开游戏!')
        return 0
    else:
        return 1

def roleChoose(num):
    temp=1
    temp = checkPlayerNum(num)
    while temp==1:
        spy=random.randint(0,num-1)
 
    #随机产生词语 定义词语列表 计算玩家票数的列表 统计死亡玩家的列表
        list_rand=randomWord()
        word=[]
        cnt=[]
        dead=[]
    #给三个列表赋值
        for i in range(0,num):
            word.append('a')
            cnt.append(0)
            dead.append(num+2)
        sy11=random.randint(0,1)
    #给玩家词语 其中print是调试用的,sanmeVote是出现相同票数的标志，spyWin是卧底胜利的判决条件
        for i in range(0,num):
             if (i==spy):
                 word[i]=str(list_rand[sy11])
             else:
                 ls=list_rand.copy()
                 ls.remove(list_rand[sy11])
                 word[i]=str(ls[0])
             print (word[i])
        tk.messagebox.showinfo('提示信息','身份已经分配完毕，游戏正式开始！')
def playsNum():
    res = askinteger("请输入游戏人数", "人数限制4—8人", initialvalue=8)
    roleChoose(res)

if __name__=='__main__':
    window = Tk()
    window.geometry('1000x700')
    b = Button(window,text='开始游戏', bg='red',width=10, height=3,command=playsNum).place(x=460,y=380,anchor='nw')
    window.mainloop()


