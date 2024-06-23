t = int(input())
for _ in range(t):
    n, f, k = map(int, input().split())
    a = list(map(int, input().split(" ")))
    b = a[f-1]
    a.sort(reverse=True)
    temporal = []

    for i in range(k):
        temporal.append(a.pop(0))
        
    if b in a and b in temporal:
        print("MAYBE")
    elif b in a and b  not in temporal:
        print("NO")
    else:
        print("YES")
    
    
