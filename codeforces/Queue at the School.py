n,t=map(int,input().split())
s=input()
s=list(s)

for x in range(0,t):
    ban=0
    for i in range(0,n-1):
        if ban==1:
            ban=0
            continue
        if s[i]=='B':
            if s[i+1]=='G':
                aux=s[i]
                s[i]=s[i+1]
                s[i+1]=aux
                ban=1

print("".join(s))

