import math
t=int(input())
for i in range(t):
    s=list(map(int,input().split()))
    maxi=max(s)
    mini=min(s)
    x=math.ceil((maxi-mini)/10)
    print(x)

