from tkinter import*
from tkinter import scrolledtext
import tkinter as tk
from tkinter import ttk
from PIL import ImageTk, Image
import random, sys
from tkinter.simpledialog import askinteger



def aa():
   def createBg():    
       testNum = tk.Button(window,text='游戏开始', bg='red',width=10, height=3,command=deplay).place(x=460,y=380,anchor='nw')
       play1 = tk.Button(window,text='1号玩家', bg='white',width=20, height=2)
       play1.place(x=0,y=326.5,anchor='nw')
       play2 = tk.Button(window,text='2号玩家',bg='white',width=20, height=2)
       play2.place(x=425,y=0,anchor='nw')
       play3 = tk.Button(window,text='3号玩家',bg='white',width=20, height=2)
       play3.place(x=850,y=326.5,anchor='nw')
       play4 = tk.Button(window,text='4号玩家',bg='white', width=20, height=2)
       play4.place(x=425,y=653,anchor='nw')
       play5 = tk.Button(window,text='5号玩家',bg='white',width=20, height=2)
       play5.place(x=0,y=0,anchor='nw')
       play6 = tk.Button(window,text='6号玩家',bg='white', width=20, height=2)
       play6.place(x=850,y=0,anchor='nw')
       play7 = tk.Button(window,text='7号玩家',bg='white', width=20, height=2)
       play7.place(x=850,y=653,anchor='nw')
       play8 = tk.Button(window,text='8号玩家',bg='white', width=20, height=2)
       play8.place(x=0,y=653,anchor='nw')
       
       '''var = tk.StringVar() # 文字变量储存器
       l = tk.Label(textvar=var,bg='white' ,width=50, height=10)
       l.place(x=320,y=440,anchor='nw')'''

   def deplay():
       res = askinteger("请输入游戏人数", "人数限制4—8人", initialvalue=8)
       roleChoose(res)

   
   window = Toplevel()
   window.title("Who's Undercover ?")
   window.geometry('1000x700')
   canvas = tk.Canvas(window, width=1000,height=699,bd=0, highlightthickness=0)
   imgpath = 'background.gif'
   img = Image.open(imgpath)
   photo = ImageTk.PhotoImage(img)
   canvas.create_image(500, 350, image=photo)
   canvas.pack()
   var = tk.StringVar()
   win.quit()
   createBg()
   window_deplay = ttk.Frame(window)
   window_deplay.place(x=400,y=480,anchor='nw')
   output = scrolledtext.ScrolledText(window, height=9, width=30, highlightbackground='black', highlightthickness=1)
   output.place(x=400,y=480,anchor='nw')
  
   window.mainloop()
  
if __name__=='__main__':
   win = Tk()
   button=Button(win,
               width=6, height=3,
              text='开始游戏',
              command=aa)

   button.place(x=350,y=200)
   win.title("进入游戏")
   win.geometry('800x500') 
   win.mainloop() 

