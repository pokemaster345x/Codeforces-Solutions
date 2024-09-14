import math

def minimun_moves(x,y,k):
    xi=math.ceil(x/k)
    yi=math.ceil(y/k)
    mini=max(yi,xi)
    
    if yi<xi:
        return (mini*2)-1
    else:
        return mini*2

t=int(input())
for i in range(t):
    x,y,k=map(int,input().split())
    print(minimun_moves(x,y,k))
