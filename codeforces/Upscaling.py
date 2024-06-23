def crea(n):
    cadena=''
    linea=''
    cont=0
    #crear primeras lineas
    for i in range (n):
        if cont==0:
            linea+='##'
            cont=1
        else:#contador ==1
            linea+='..'
            cont=0
    #linea segunda
    lineainverse=''
    cont=0
    for i in range (n):
        if cont==0:
            lineainverse+='..'
            cont=1
        else:#contador ==1
            lineainverse+='##'
            cont=0
    cont=0
    for x in range(n):
        if cont==0:
            cadena+=linea+'\n'
            cadena+=linea+'\n'
            cont=1
        else:
            cadena+=lineainverse+'\n'
            cadena+=lineainverse+'\n'
            cont=0
    return cadena[:-1]
t=int(input())

for i  in range(t):
    n=int(input())
    print(crea(n))
    