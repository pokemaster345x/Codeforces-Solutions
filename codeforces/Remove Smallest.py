def pepe(test_cases):
    results = []
    for a in test_cases:
        a.sort()
        possible = True
        for i in range(len(a) - 1):
            if a[i + 1] - a[i] > 1:
                possible = False
                break
        if possible:
            results.append("YES")
        else:
            results.append("NO")
    return results

t = int(input())
test_cases = []
for _ in range(t):
    n = int(input())
    a = list(map(int, input().split()))
    test_cases.append(a)

results = pepe(test_cases)

for result in results:
    print(result)
