from collections import deque

bd = []

q = deque()
q.append(1)

while q:
    front = q.popleft()
    if front != 1:
        bd.append(front)

    if front > 10**5 + 5:
        break

    q.append(front*10)
    q.append(front*10 + 1)

bd.reverse()

t = int(input())
for _ in range(t):
    n = int(input())
    ans = "NO"

    for x in bd:
        while n % x == 0:
            n //= x

    if n == 1:
        ans = "YES"
    
    print(ans)
