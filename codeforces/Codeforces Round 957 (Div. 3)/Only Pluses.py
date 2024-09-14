t=int(input())
for i in range(t):
    s=list(map(int,input().split()))
    for i in range(5):
        s.sort()
        s[0]+=1
    ans=s[0]*s[1]*s[2]
    print(ans)