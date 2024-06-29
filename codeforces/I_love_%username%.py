n=int(input())
numbers=list(map(int,input().split()))
min=max=numbers[0]
aux=0
for i in range(1,n):
    if numbers[i]<min:
        min=numbers[i]
        aux+=1
    elif numbers[i]>max:
        max=numbers[i]
        aux+=1
print(aux)