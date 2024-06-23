xd=int(input())
a=input()
contA=0
contD=0
for i in a:
    if i=='A':
        contA+=1
    else:
        contD+=1
    if contA>(xd/2):
        print("Anton")
        break
    if contD>(xd/2):
        print("Danik")
        break
if contA==contD:
    print("Friendship")