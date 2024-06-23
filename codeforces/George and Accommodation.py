n=int(input())
cont=0
for i in range(n):
    p,q=map(int,input().split())
    if q-p >=2:
        cont+=1
print(cont)