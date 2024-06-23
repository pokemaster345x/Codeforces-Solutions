a=input()
cont0=0
cont1=0
boleano=False
for i in a:
    if i=='0':
        cont0+=1
        cont1=0
    else:
        cont1+=1
        cont0=0
    if cont0==7 or cont1==7:
        print("YES")
        boleano=True
        break
if boleano==False:
    print("NO")