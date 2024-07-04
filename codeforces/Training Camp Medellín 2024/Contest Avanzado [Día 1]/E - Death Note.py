def idk(n, m, a):
    pag = 0
    rest = []
    for x in a:
        nombres =  pag+ x
        xd = nombres // m
        pag = nombres % m
        rest.append(xd)
    return rest
n, m = map(int, input().split())
a = list(map(int, input().split()))
print(" ".join(map(str, idk(n, m, a))))
