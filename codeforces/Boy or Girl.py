a=input()
vocalesusadas=[]
xd=0
for i in a:
    if i not in vocalesusadas:
        xd+=1
        vocalesusadas.append(i)
if xd%2==0:
    print("CHAT WITH HER!")
else:
    print("IGNORE HIM!")