
import random
from spyword import spyword
 
num=int(input('请输入玩家数（至少为3）\n'))
#卧底玩家
spy=random.randint(0,num-1)
 
#随机产生词语 定义词语列表 计算玩家票数的列表 统计死亡玩家的列表
list_rand=spyword.popitem()
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
sameVote=0
spyWin=0
#游戏开始
for x in range(0,num-1):
	for k in range(0,num):
		if ((k not in dead) & (sameVote==0)):
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
		
#游戏结束
if(spyWin==0):
	print ('只剩两名玩家，卧底胜利！')
