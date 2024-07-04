def mueltos(s):
    n=len(s)
    bombillasmueltas={'R':0,"B":0,"Y":0,"G":0}
    posiciones={'R':-10,"B":-10,"Y":-10,"G":-10}
    for i in range(n):
        if s[i] in posiciones:
            posiciones[s[i]]=i%4
    for i in range(n):
        if s[i]=='!':
            pos=i%4
            for color,p in posiciones.items():
                if p==pos:
                    bombillasmueltas[color]+=1
    return bombillasmueltas["B"],bombillasmueltas["R"],bombillasmueltas["Y"],bombillasmueltas['G']
            
s=list(map(str,input().split()))
print(" ".join(map(str, mueltos(s))))