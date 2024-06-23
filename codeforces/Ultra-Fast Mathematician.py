s=input()
x=input()
result=''
for i in range(len(s)):
    result+=str(abs(-(int(s[i]))+(int(x[i]))))
print(result)