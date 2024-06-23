import time
a=input()
inicio=time.time()
b=[]
frist=a[0]
frist=frist.upper()
xd=str(frist)
for i in range(1,(len(a))):
    b.append(a[i])
xd=xd+''.join(b)
print(xd)
fin=time.time()
print(fin-inicio)
