a=input()
b="AEIOUYaeiouy"
a=a.lower()
xd=[]
for caracter in a:
    if caracter in b:
        continue
    xd.append('.')
    if caracter.isupper():
        caracter=caracter.lower()
    xd.append(caracter)
salida=''.join(xd)
print(salida)