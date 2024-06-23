a=input()
b="hello"
aux=0
for i in range(len(a)):
    if a[i]==b[aux]:
        aux+=1
    if aux==5:
        break
if aux==5:
    print("YES")
else:
    print("NO")