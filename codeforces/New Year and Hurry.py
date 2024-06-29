
n,k=map(int,input().split())
minutos=240
minutos-=k
suma=0
while(True):
    suma=(5*n*(n+1))//2
    if suma<=minutos:
        break

    n-=1
print(n) 
