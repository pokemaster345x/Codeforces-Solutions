n=int(input())
entrada=''
x=y=z=0
for i in range(0,n):
    entrada=input()
    entrada=entrada.split()
    for a in range(0,3):
        entrada[a]=int(entrada[a])
    x+=entrada[0]
    y+=entrada[1]
    z+=entrada[2]
if x!=0 or y!=0 or z!=0:
    print("NO")
else:
    print("YES")
    
    