k=int(input())
l=int(input())
m=int(input())
n=int(input())
d=int(input())
aux=[]
auxk=d//k
auxl=d//l
auxm=d//m
auxn=d//n
for i in range(1,auxk+1):
    aux.append(k*i)
for i in range(1,auxl+1):
    aux.append(l*i)
for i in range(1,auxm+1):
    aux.append(m*i)
for i in range(1,auxn+1):
    aux.append(n*i)

print(len(set(aux)))