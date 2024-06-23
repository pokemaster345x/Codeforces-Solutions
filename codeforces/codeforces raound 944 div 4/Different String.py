def isdiferent(r):
    if len(set(r))==1:
        print("NO")
    else:
        print("YES\n"+ r[1:] + r[0])



n=int(input())
for i in range(n):
    r=input()
    isdiferent(r)
    