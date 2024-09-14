t=int(input())
for i in range(t):
    ans=0
    n,k=map(int,input().split())
    s=list(map(int,input().split()))
    s.sort()
    ans=n-(s[k-1])
    for x in range(0,k-1):
        if s[x]==1:
            continue
        else:
            ans+=s[x]-1
    print(ans)

