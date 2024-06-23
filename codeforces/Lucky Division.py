n = int(input())
s = set(str(n))  
if len(s) == 2 and (('7' in s and '4' in s) or ('7' in s and '4' in s)):
    print("YES")
elif n % 4 == 0 or n % 7 == 0 or n%47==0 or n%74==0:
    print("YES")
else:
    print("NO")
