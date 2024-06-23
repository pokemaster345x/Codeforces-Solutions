a=int(input())
aux=0
for i in range(a):
    b=input()
    b=b.split()
    c=int(b[0])+int(b[1])+int(b[2])
    if c>1:
        aux+=1
print(aux)