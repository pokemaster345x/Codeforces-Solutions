def mueltos(s):
    n=len(s)
    bombillasmuertas={'R': 0, 'B': 0, 'Y': 0, 'G': 0}
    posiciones={'R': -10, 'B': -10, 'Y': -10, 'G': -10}
    for i in range(n):
        if s[i] in posiciones:
            posiciones[s[i]]=i%4
    for i in range(n):
        if s[i]=='!':
            pos=i%4
            for color,p in posiciones.items():
                if p==pos:
                    bombillasmuertas[color]+=1
    return bombillasmuertas['R'],bombillasmuertas['B'],bombillasmuertas['Y'],bombillasmuertas['G']


s = input().strip()
print(" ".join(map(str, mueltos(s))))
