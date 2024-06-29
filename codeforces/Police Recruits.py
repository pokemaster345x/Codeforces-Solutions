n=int(input())
sinrevisar=0
policias_activos=0
entrada=list(map(int,input().split()))
for i in range(n):
    
    if entrada[i]>0:
        policias_activos+=entrada[i]
    elif policias_activos<1:
        sinrevisar+=1
    else:
        policias_activos-=1
print(sinrevisar)