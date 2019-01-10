from tkinter import *
from tkinter import scrolledtext
import tkinter as tk
from tkinter import ttk
from PIL import ImageTk, Image
import random, sys
from tkinter.simpledialog import askinteger


def randomWord():
    fo=open("wd.txt","r")
    for line  in  fo:
        a=line.replace(';',' ')
        a=a.split( )
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
        word=[]
        cnt=[]
        dead=[]
    #给三个列表赋值
        for i in range(0,num):
            word.append('a')
            cnt.append(0)
            dead.append(num+2)
 
    #给玩家词语 其中print是调试用的,sanmeVote是出现相同票数的标志，spyWin是卧底胜利的判决条件
        for i in range(0,num):
            if (i==spy):
                word[i]=str(list_rand[1])
            else:
                word[i]=str(list_rand[0])
            print (word[i])
        tk.messagebox.showinfo('提示信息','身份已经分配完毕，游戏正式开始！')
        gameBegin(num,word,cnt,dead,spy)

def gameBegin(num,word,cnt,dead,spy):
    
    sameVote=0
    spyWin=0
   

    for x in range(0,num-2):
        for k in range(0,num):
            if ((k not in dead) & (sameVote==0)):
                output.insert(tk.INSERT, '请%d号玩家发言！\n' %(k+1))
                tk.messagebox.askyesno(title='发言阶段',message='%d号玩家发言是否结束'%(k+1))
        tk.messagebox.showinfo('提示信息','所有玩家发言完毕，请依次点击投票按钮！')
		
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
            output.insert(tk.INSERT, '%d号玩家被冤死!\n'%(dead[x]+1))
    GameOver(spyWin)
    



def GameOver(spyWin):
    if(spyWin==0):
        tk.messagebox.showinfo('游戏结束','卧底胜利！\n平民继续加油哦！')

    again = askinteger("还想再来吗？", "再来一局请输0\n退出请输入1", initialvalue=0)
    if again == 1:
        sys.exit()


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
 
