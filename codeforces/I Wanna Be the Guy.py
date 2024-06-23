n=int(input())
p=list(map(int,input().split()))

xd=[]
for i in range(1,p[0]+1):
    xd.append(p[i])
q=list(map(int,input().split()))
for i in range(1,q[0]+1):
    xd.append(q[i])
xd=set(xd)
if len(xd)==n:
    print("I become the guy.")
else:
    print("Oh, my keyboard!")