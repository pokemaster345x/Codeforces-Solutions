def ronda(banco, dic, m):
    problems_needed = 0
    for difficulty in dic:
        problems_needed += max(0, m - banco.count(difficulty))
    return problems_needed

t = int(input())

for _ in range(t):
    n, m = map(int, input().split())
    banco = list(input().strip())
    dic = ['A', 'B', 'C', 'D', 'E', 'F', 'G']
    problems_needed = ronda(banco, dic, m)

    print(problems_needed)