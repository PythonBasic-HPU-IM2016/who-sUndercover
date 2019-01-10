import random

def aaa():
    fo=open("wd.txt","r")
    for line  in  fo:
        a=line.replace(';',' ')
        a=a.split( )
        num=len(a)
    spy=random.randint(0,num-1)

    b=a[spy].replace('-',' ')
    b=b.split( )
    return b
t = aaa()
print(t)
