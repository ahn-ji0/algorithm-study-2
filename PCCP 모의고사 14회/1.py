# 줄 세우기 - https://www.acmicpc.net/problem/2631

N = int(input())
child = [int(input()) for i in range(N)]

dp = [1 for i in range(N)]
for i in range(N-2, -1, -1):
    max_val = 0
    for j in range(i + 1, N):
        if child[j] > child[i] and dp[j] > max_val:
            max_val = dp[j]

    dp[i] = max_val + 1
# print(dp)
print(N - max(dp))
