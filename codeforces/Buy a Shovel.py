k,n=map(int,input().split())
aux=1
saurio=(k*aux)%10
while saurio!=0 and saurio!=n:
    aux+=1
    saurio=(k*aux)%10
print(aux)
