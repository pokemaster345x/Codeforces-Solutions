a=input()
a=a.split("+")
b=[]
xd=''
for i in range(0,len(a)):
    a[i]=int(a[i])
a.sort()
b.append(str(a[0]))
for i in range(1,len(a)):
    b.append("+")
    b.append(str(a[i]))
xd=xd.join(b)
print(xd)

