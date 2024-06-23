n,h=map(int, input().split())
a=map(int, input().split())
cont=0
for i in a:
    if i>h:
        cont+=2
    else:
        cont+=1
print(cont)