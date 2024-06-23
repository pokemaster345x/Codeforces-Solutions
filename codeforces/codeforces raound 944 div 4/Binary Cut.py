def nose(s):
    cont = 0
    lista = s.split("0")
    for i in range(1, len(lista)):
        lista[i] = "0" + lista[i]

    lista = list(set(lista))
    lista.sort()
    print(lista)
    if "" in lista:
        cont += 1
    for i in range(1, len(lista)):
        if lista[i] == "0":
            cont += 1
    return len(lista) - cont

t = int(input())
for i in range(t):
    s = input()
    print(nose(s))