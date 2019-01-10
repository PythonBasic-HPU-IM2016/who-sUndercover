def aaa():
    fo=open("C:\\Users\\deng\\AppData\\Local\\Programs\\Python\\Python37\\python12\\111.txt","r")
    for line  in  fo:
        a=line.replace(';',' ')
        a=a.split( )
        num=len(a)
    spy=random.randint(0,num-1)

    b=a[spy].replace('-',' ')
    b=b.split( )
    return b
