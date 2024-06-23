a=input()
upers=0
lowers=0
for i in a:
    if i.isupper():
        upers+=1
    else:
        lowers+=1
if upers>lowers:
    print(a.upper())
else:
    print(a.lower())