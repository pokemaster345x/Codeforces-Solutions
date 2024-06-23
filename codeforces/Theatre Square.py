a=input()
a=a.split()
a=[int(i) for i in a]
xint=(a[0])//a[2]
xfloat=a[0]/a[2]
yint=a[1]//a[2]
yfloat=a[1]/a[2]
if xfloat>xint:
    xint+=1
if yfloat>yint:
    yint+=1
print(xint*yint)
