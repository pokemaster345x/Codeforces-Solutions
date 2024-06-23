def pepesaurio(x1,x2,x3):
    resultado=''
    ordenados=sorted([x1,x2,x3])
    mediana=ordenados[1]
    resultado=abs(mediana-x1)+abs(mediana-x2)+abs(mediana-x3)
    return resultado
t=int(input())
for i in range(t):
    x1,x2,x3=map(int,input().split())
    print(pepesaurio(x1,x2,x3))
