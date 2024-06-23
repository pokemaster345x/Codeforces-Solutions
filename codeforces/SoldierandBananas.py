xd=input()
xd=xd.split()
x=0
for i in range(0,3):
    xd[i]=int(xd[i])
for i in range(1,(xd[2]+1)):
    x+=i*xd[0]
if x<=xd[1]:
    print(0)
else:
    print(x-xd[1])