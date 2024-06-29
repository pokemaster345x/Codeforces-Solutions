xs=list(map(int,input().split()))
xs=sorted(xs)
result=abs(xs[1]-xs[0])+abs(xs[1]-xs[2])
print(result)
