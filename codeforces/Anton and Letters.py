s=input()
aux=0
no_contar=["{",",","}"," "]
contadas=[]
for i in s:
    if i in no_contar:
        continue
    elif i not in contadas:
        aux+=1
        contadas.append(i)
print(aux)