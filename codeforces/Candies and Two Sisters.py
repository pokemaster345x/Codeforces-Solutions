"""def yoquese(n): forma bruta y lenta
    a=n-1
    b=1
    cont=0
    while a>b:
        a-=1
        b+=1
        cont+=1
    return cont"""
def yoquese(n):
    
    return (n-1)//2
t=int(input())
for i in range(t):
    n=int(input())
    print(yoquese(n))

t=int(input())
for i in range(t):
    n=int(input())
    print(yoquese(n))
