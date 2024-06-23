n=int(input())
home=[]
visitante=[]
aux=0
for i in range(n):
    h,a=map(int,input().split())
    home.append(h)
    visitante.append(a)
for i in home:
    aux+=visitante.count(i)
print(aux)

