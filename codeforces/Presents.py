n = int(input())
i = list(map(int, input().split()))
xd = [0] * n

for x in range(n):
    xd[i[x] - 1] = x + 1

waos = ' '.join(map(str, xd))  
print(waos)
