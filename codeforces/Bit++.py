a= int(input())
z=0
for i in range(a):
    x=input()
    if "+" in x:
        z+=1
    else:
        z-=1
print(z)
