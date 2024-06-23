a = input()
a = a.split()
b = input()
b = b.split()
b = [int(i) for i in b]
n = int(a[0])
k = int(a[1])
aux = 0
aux1 = int(b[k-1])  
for i in range(n):
    if b[i] >= aux1 and b[i] > 0:
        aux += 1
print(aux)
