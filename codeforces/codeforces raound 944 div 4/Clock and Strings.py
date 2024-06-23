def is_empty(a,b,c,d):
    mayor=0
    menor=0
    cont=0
    if a>b:
        mayor=a
        menor=b
    else:
        mayor=b
        menor=a
    i=menor
    while(i<=mayor):
        if i==c or i==d:
            cont+=1
        i+=1
    return cont

t=int(input())
for i in range(t):
    a,b,c,d=map(int, input().split())
    if is_empty(a,b,c,d)==1:
        print("YES")
    else: 
        print("NO")