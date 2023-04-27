MAX = 31
dp = [[1 for i in range(MAX)] for j in range(MAX)]
for i in range(0, MAX - 1):
    total = 0
    for j in range(i+1):
        total += dp[i][j]
        if j == 0:
            continue

        dp[i+1][j] = total
        if j == i:
            dp[i+1][j+1] = total

while True:
    N = int(input())
    if N == 0:
        break
    print(dp[N][N])