n=int(input())
p=map(int,input().split())
sum=0
for i in p:
    sum+=i
result=sum/n
print(result)