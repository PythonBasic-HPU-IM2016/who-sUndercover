from tkinter import*
import tkinter as tk
from PIL import ImageTk, Image
import random, sys
from tkinter.simpledialog import askinteger




def roleChoose(num):
    spy=random.randint(0,num-1)
 
    #随机产生词语 定义词语列表 计算玩家票数的列表 统计死亡玩家的列表
    list_rand=['玻璃','眼镜']
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
    
    gameBegin(num,word,cnt,dead,spy)

def gameBegin(num,word,cnt,dead,spy):
    
    sameVote=0
    spyWin=0
    for x in range(0,num-1):
        for k in range(0,num):
            if ((k not in dead) & (sameVote==0)):
                tk.messagebox.askyesno(title='发言阶段',message='发言是否结束')
                print ('%d号玩家发言时间'%(k+1))
            print ('发言环节结束')
		
	#将各位玩家的票数置0
        for j in range(0,num):
            if (j not in dead):
                cnt[j]=0
        for j in range(0,num):
            if (j not in dead):
                vote2p=int(input('请%d号玩家投票'%(j+1)))-1
                cnt[vote2p]=cnt[vote2p]+1
                sameVote=0
        for y in range(0,num):
            if((cnt[y]==max(cnt)) & (y!=cnt.index(max(cnt)))):
                print ('不止一位玩家得到最高票数,请这些玩家重新发言')
                sameVote=1
        if (sameVote==0):
            dead[x]=cnt.index(max(cnt))
            if (dead[x]==spy):
                print ('卧底得到最多票数，游戏结束')
                spyWin=1
                break
            print ('%d号玩家被冤死!'%(dead[x]+1))
    GameOver(spyWin)
def GameOver(spyWin):
    if(spyWin==0):
        print("只剩两名玩家，卧底胜利！")


   


def createBg(): 
    
    
    testNum = tk.Button(text='游戏开始', bg='red',width=10, height=3,command=deplay).place(x=460,y=380,anchor='nw')
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
    testNum = tk.Button(text='8号玩家',bg='white', width=10, height=5).place()
    '''var = tk.StringVar() # 文字变量储存器
    l = tk.Label(textvar=var,bg='white' ,width=50, height=10)
    l.place(x=320,y=440,anchor='nw')'''

def deplay():
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
    var = tk.StringVar()
    createBg()
    
    window.mainloop()
 
