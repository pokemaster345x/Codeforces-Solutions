t=int(input())

for i in range(t):
    aux=0
    respuesta=[]
    n=int(input())
    leng=len(str(n))
    for x in range(leng):
        aux=n%10**(x+1)
        if aux!=0:
            respuesta.append(aux)
            n-=aux
    print(len(respuesta))
    xd = ' '.join(map(str, respuesta))
    print(xd)