from tkinter import *
from tkinter import scrolledtext
import tkinter as tk
from tkinter import ttk
from PIL import ImageTk, Image
import random, sys
from tkinter.simpledialog import askinteger



def createBg(): 
     
    play1 = tk.Button(text='1号玩家', bg='white',width=20, height=2)
    play1.place(x=0,y=326.5,anchor='nw')
    play2 = tk.Button(text='2号玩家',bg='white',width=20, height=2)
    play2.place(x=425,y=0,anchor='nw')
    play3 = tk.Button(text='3号玩家',bg='white',width=20, height=2)
    play3.place(x=850,y=326.5,anchor='nw')
    play4 = tk.Button(text='4号玩家',bg='white', width=20, height=2)
    play4.place(x=425,y=653,anchor='nw')
    play5 = tk.Button(text='5号玩家',bg='white',width=20, height=2)
    play5.place(x=0,y=0,anchor='nw')
    play6 = tk.Button(text='6号玩家',bg='white', width=20, height=2)
    play6.place(x=850,y=0,anchor='nw')
    play7 = tk.Button(text='7号玩家',bg='white', width=20, height=2)
    play7.place(x=850,y=653,anchor='nw')
    play8 = tk.Button(text='8号玩家',bg='white', width=20, height=2)
    play8.place(x=0,y=653,anchor='nw')

    

    '''var = tk.StringVar() # 文字变量储存器
    l = tk.Label(textvar=var,bg='white' ,width=50, height=10)
    l.place(x=320,y=440,anchor='nw')'''

def playsNum():
    '''if b['text'] == '开始游戏':
        v.set('重开游戏')
    else:
        v.set('开始游戏')'''
    res = askinteger("请输入游戏人数", "人数限制4—8人", initialvalue=8)
    roleChoose(res)

if __name__=='__main__':
    window = Tk()
    window.title("Who's Undercover ?")
    window.geometry('1000x700')
    canvas = tk.Canvas(window, width=1000,height=699,bd=0, highlightthickness=0)
    imgpath = 'background.gif'
    img = Image.open(imgpath)
    photo = ImageTk.PhotoImage(img)
    canvas.create_image(500, 350, image=photo)
    canvas.pack()
    createBg()
  
    window_deplay = ttk.Frame(window)
    window_deplay.place(x=400,y=480,anchor='nw')
    output = scrolledtext.ScrolledText(window, height=9, width=30, highlightbackground='black', highlightthickness=1)
    output.place(x=400,y=480,anchor='nw')
    v = StringVar()
    v.set('开始游戏')
    b = Button(window,textvariable=v, bg='red',width=10, height=3,command=playsNum).place(x=460,y=380,anchor='nw')
     
    window.mainloop()
