n, m = map(int, input().split())

cadenas = [''] * 3  
cadenas[0] = '#'
cadenas[1] = '.'
cadenas[2] = '#'

for i in range(1, m):
    cadenas[0] += '#'
    if i == (m- 1):
        cadenas[1] += '#'
    else:
        cadenas[1] += '.'
    cadenas[2] += '.'
aux=0

for i in range(n):
    if i%2==0:
        print(cadenas[0])
    elif aux==0:
        print(cadenas[1])
        aux=1
    else:
        print(cadenas[2])
        aux=0


