n=int(input())
a=list(map(int,input().split()))
maximo=max(a)
minimo=min(a)
cont=0
compepe=0
while(True):
    if a[0]==maximo:
        break
    for i in range(n):
        if a[i]==maximo:
            aux=a[i-1]
            a[i-1]=a[i]
            a[i]=aux
            cont+=1
            break
while(True):
    if a[len(a)-1]==minimo:
        break
    for x in range(n-1,-1,-1):
        if a[x]==minimo:
            aux=a[x+1]
            a[x+1]=a[x]
            a[x]=aux
            cont+=1
            break
print(cont)