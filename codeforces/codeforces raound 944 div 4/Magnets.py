n=int(input())
cont=0
i=input()
aux=i[1]
for x in range(n-1):
    if i[0]==aux:
        cont+=1
    i=input()
    aux=i[1]
    
print(cont)