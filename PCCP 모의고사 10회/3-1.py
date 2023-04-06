# 동전 1 - https://www.acmicpc.net/problem/2293
# DP* - 성공

N, K = map(int, input().split())
coins = [int(input()) for i in range(N)]
dp = [0 for i in range(K+1)]
dp[0] = 1

for coin in coins:
    for i in range(coin, K+1):
        prev = dp[i-coin]
        dp[i] += prev

print(dp[K])