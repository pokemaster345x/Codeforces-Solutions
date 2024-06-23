c, n = map(int, input().split())
songs = list(map(int, input().split()))
songs.sort(reverse=True)

dp = [[0] * (c + 1) for _ in range(2)]
for i in range(1, n + 1):
    for j in range(c + 1):
        dp[i % 2][j] = dp[(i - 1) % 2][j]
        if j >= songs[i - 1] and dp[(i - 1) % 2][j - songs[i - 1]] + songs[i - 1] > dp[i % 2][j]:
            dp[i % 2][j] = dp[(i - 1) % 2][j - songs[i - 1]] + songs[i - 1]

cd1 = dp[n % 2][c]
cd2 = sum(songs) - cd1

if cd1 >= cd2:
    print(cd1, cd2)
else:
    print(cd2, cd1)
