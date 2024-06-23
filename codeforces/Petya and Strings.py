abecedario=["a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","w","x","y","z"]
a= input().lower()
b= input().lower()
if a==b:
    print(0)
else:
    for i in range(len(a)):
        if abecedario.index(a[i])>abecedario.index(b[i]):
            print(1)
            break
        elif abecedario.index(a[i])<abecedario.index(b[i]):
            print(-1)
            break
    else:
        print(0)