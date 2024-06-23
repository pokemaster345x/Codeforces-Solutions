lines= int(input())
capmin=0
capamax=0
for i in range(0,lines):
    entrada=input()
    entrada=entrada.split()
    capmin-=int(entrada[0])
    capmin+=int(entrada[1])
    if capamax<capmin:
        capamax=capmin
print(capamax)