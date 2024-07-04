n=int(input())

a=list(map(int,input().split()))
maximo=max(a)
acum=0
for i in a:
    acum+=abs(maximo-i)
print(acum)
