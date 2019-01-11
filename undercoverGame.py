from tkinter import *
from tkinter import scrolledtext
import tkinter as tk
from tkinter import ttk
from PIL import ImageTk, Image
import random, sys
from tkinter.simpledialog import askinteger
import pygame
import time

def colorTurn3(m):
    if m == 1:
        play1['text']='1号选手死亡'
        play1['bg']='green'
    elif m == 2:
        play2['text']='2号选手死亡'
        play2['bg']='green'
    elif m == 3:
        play3['text']='3号选手死亡'
        play3['bg']='green'
    elif m == 4:
        play4['text']='4号选手死亡'
        play4['bg']='green'
    elif m == 5:
        play5['text']='5号选手死亡'
        play5['bg']='green'
    elif m == 6:
        play6['text']='6号选手死亡'
        play6['bg']='green'
    elif m == 7:
        play7['text']='7号选手死亡'
        play7['bg']='green'
    elif m == 8:
        play8['text']='8号选手死亡'
        play8['bg']='green'

def colorTurn2(m):
    if m == 1:
        play1['text']='1号选手发言完毕'
        play1['bg']='yellow'
    elif m == 2:
        play2['text']='2号选手发言完毕'
        play2['bg']='yellow'
    elif m == 3:
        play3['text']='3号选手发言完毕'
        play3['bg']='yellow'
    elif m == 4:
        play4['text']='4号选手发言完毕'
        play4['bg']='yellow'
    elif m == 5:
        play5['text']='5号选手发言完毕'
        play5['bg']='yellow'
    elif m == 6:
        play6['text']='6号选手发言完毕'
        play6['bg']='yellow'
    elif m == 7:
        play7['text']='7号选手发言完毕'
        play7['bg']='yellow'
    elif m == 8:
        play8['text']='8号选手发言完毕'
        play8['bg']='yellow'


def colorTurn1(m):
    if m == 1:
        play1['text']='1号选手发言中'
        play1['bg']='red'
    elif m == 2:
        play2['text']='2号选手发言中'
        play2['bg']='red'
    elif m == 3:
        play3['text']='3号选手发言中'
        play3['bg']='red'
    elif m == 4:
        play4['text']='4号选手发言中'
        play4['bg']='red'
    elif m == 5:
        play5['text']='5号选手发言中'
        play5['bg']='red'
    elif m == 6:
        play6['text']='6号选手发言中'
        play6['bg']='red'
    elif m == 7:
        play7['text']='7号选手发言中'
        play7['bg']='red'
    elif m == 8:
        play8['text']='8号选手发言中'
        play8['bg']='red'

def roleCheck(m):
    if m == 1:
        play1['text']='1号选手身份确认完毕'
        play1['bg']='blue'
    elif m == 2:
        play2['text']='2号选手身份确认完毕'
        play2['bg']='blue'
    elif m == 3:
        play3['text']='3号选手身份确认完毕'
        play3['bg']='blue'
    elif m == 4:
        play4['text']='4号选手身份确认完毕'
        play4['bg']='blue'
    elif m == 5:
        play5['text']='5号选手身份确认完毕'
        play5['bg']='blue'
    elif m == 6:
        play6['text']='6号选手身份确认完毕'
        play6['bg']='blue'
    elif m == 7:
        play7['text']='7号选手身份确认完毕'
        play7['bg']='blue'
    elif m == 8:
        play8['text']='8号选手身份确认完毕'
        play8['bg']='blue'


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
        global word
        word =[0,0,0,0,0,0,0,0]
        cnt=[]
        dead=[]
    #给三个列表赋值
        for i in range(0,num):
            
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
            tk.messagebox.showwarning('提示信息','请%d号玩家检验身份！'%(i+1))
            change(i+1)
            tk.messagebox.showwarning('提示信息','%d号玩家检验身份是否结束！'%(i+1))
            roleCheck(i+1)
        tk.messagebox.showinfo('提示信息','身份已经分配完毕，游戏正式开始！')
        gameBegin(num,word,cnt,dead,spy)

def gameBegin(num,word,cnt,dead,spy):
    
    sameVote=0
    spyWin=0
   

    for x in range(0,num-2):
        for k in range(0,num):
            if ((k not in dead) & (sameVote==0)):
                colorTurn1(k+1)
                output.insert(tk.INSERT, '请%d号玩家发言！\n' %(k+1))
                pygame.mixer.music.load("%d.mp3"%(k+1))
                pygame.mixer.music.play(1)
                #time.sleep(10)
                tk.messagebox.showinfo('发言阶段','%d号玩家发言是否结束'%(k+1))
                colorTurn2(k+1)
                #tk.messagebox.askyesno(title='发言阶段',message='%d号玩家发言是否结束'%(k+1))

        pygame.mixer.music.load("toupiao.mp3")
        pygame.mixer.music.play(1)
        tk.messagebox.showinfo('提示信息','所有玩家发言完毕，请依次开始投票！')
        bgSound.load("bg.mp3")      
        bgSound.play(-1) 
	#将各位玩家的票数置0
        
        for j in range(0,num):
            cnt[j]=0
        for j in range(0,num):
            if (j not in dead):
                piaoNum = askinteger("%d号玩家投票中"%(j+1), "请输入你认为是卧底的玩家序号", initialvalue=8)
                vote2p=int(piaoNum)-1
                cnt[vote2p]=cnt[vote2p]+1
                sameVote=0
        for y in range(0,num):
            if((cnt[y]==max(cnt)) & (y!=cnt.index(max(cnt)))):
                tk.messagebox.showinfo('游戏提示信息','不止一位玩家得到最高票数,请这些玩家重新发言！')
                sameVote=1
        if (sameVote==0):
            dead[x]=cnt.index(max(cnt))
            if (dead[x]==spy):
                tk.messagebox.showinfo('游戏结束','平民胜利，游戏结束！\n卧底继续加油哦！')
                spyWin=1
                break
            tk.messagebox.showinfo('投错人咯！！！','%d号玩家被冤死!\n'%(dead[x]+1))
            colorTurn3(dead[x]+1)
            output.insert(tk.INSERT, '%d号玩家被冤死!\n'%(dead[x]+1))
    GameOver(spyWin)
    



def GameOver(spyWin):
    if(spyWin==0):
        tk.messagebox.showinfo('游戏结束','卧底胜利！\n平民继续加油哦！')

    answer = tk.messagebox.askquestion("Game","再来一局吗?")
    if answer == "no":
        pygame.mixer.music.stop()
        window.destroy()
        sys.exit()
    else:
        createBg()
        
def change(i):
    if i==1:
        play1['text']=word[i-1]
    elif i==2:
        play2['text']=word[i-1]
    elif i==3:
        play3['text']=word[i-1]
    elif i==4:
        play4['text']=word[i-1]
    elif i==5:
        play5['text']=word[i-1]
    elif i==6:
        play6['text']=word[i-1]
    elif i==7:
        play7['text']=word[i-1]
    else:
        play8['text']=word[i-1]                     
    

def createBg():
    
    global play1,play2,play3,play4,play5,play6,play7,play8 
    play1 = tk.Button(text='1号玩家', bg='white',width=20, height=2,command=lambda:change(1))
    play1.place(x=0,y=326.5,anchor='nw')
    play2 = tk.Button(text='2号玩家',bg='white',width=20, height=2,command=lambda:change(2))
    play2.place(x=425,y=0,anchor='nw')
    play3 = tk.Button(text='3号玩家',bg='white',width=20, height=2,command=lambda:change(3))
    play3.place(x=850,y=326.5,anchor='nw')
    play4 = tk.Button(text='4号玩家',bg='white', width=20, height=2,command=lambda:change(4))
    play4.place(x=425,y=653,anchor='nw')
    play5 = tk.Button(text='5号玩家',bg='white',width=20, height=2,command=lambda:change(5))
    play5.place(x=0,y=0,anchor='nw')
    play6 = tk.Button(text='6号玩家',bg='white', width=20, height=2,command=lambda:change(6))
    play6.place(x=850,y=0,anchor='nw')
    play7 = tk.Button(text='7号玩家',bg='white', width=20, height=2,command=lambda:change(7))
    play7.place(x=850,y=653,anchor='nw')
    play8 = tk.Button(text='8号玩家',bg='white', width=20, height=2,command=lambda:change(8))
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
    #新建窗口
    window = Tk()
    window.title("Who's Undercover ?")
    #设置窗口大小
    window.geometry('1000x700')
    '''
    定义一个画布背景
    在背景内插入image
    '''
    canvas = tk.Canvas(window, width=1000,height=699,bd=0, highlightthickness=0)
    imgpath = 'background.gif'
    #打开照片的相关操作
    img = Image.open(imgpath)
    photo = ImageTk.PhotoImage(img)
    canvas.create_image(500, 350, image=photo)
    canvas.pack()

    #利用pygame库，作为背景音的载体
    pygame.init()   
    pygame.mixer.init()   
    pygame.time.delay(500)#等待让mixer完成初始化   
    bgSound = pygame.mixer.music#载入音乐的引入方法
    bgSound.load("bg.mp3")      
    bgSound.play(-1)#播放次数，正n为n次，-1无限循环
    createBg()
    window_deplay = ttk.Frame(window)
    window_deplay.place(x=400,y=480,anchor='nw')
    output = scrolledtext.ScrolledText(window, height=9, width=30, highlightbackground='black', highlightthickness=1)
    output.place(x=400,y=480,anchor='nw')
    v = StringVar()
    v.set('开始游戏')
    b = Button(window,textvariable=v, bg='red',width=10, height=3,command=playsNum).place(x=460,y=380,anchor='nw')
     
    window.mainloop()
 
