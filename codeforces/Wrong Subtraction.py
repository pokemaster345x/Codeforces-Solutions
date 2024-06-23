a=input()
a=a.split()
a[0]=int(a[0])
a[1]=int(a[1])
for i in range (0,a[1]):
    if a[0]%10 ==0:
        a[0]=a[0]//10
    else:
        a[0]-=1
print(a[0])