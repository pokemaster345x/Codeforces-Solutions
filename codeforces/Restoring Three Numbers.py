xs=list(map(int,input().split()))
xs.sort()
#3 4 5 6 
a=xs[3]-xs[2]#a=1
b=xs[1]-a #b=3
c=xs[2]-b #c=2
print(str(a)+" "+str(b)+" "+str(c))
