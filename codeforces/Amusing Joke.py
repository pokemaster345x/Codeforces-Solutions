s1=list(input())
s2=list(input())
s3=list(input())
aux=[]
for i in s1:
    aux.append(i)
for i in s2:
    aux.append(i)
aux.sort()
s3.sort()
if s3==aux:
    print("YES")
else:
    print("NO")
