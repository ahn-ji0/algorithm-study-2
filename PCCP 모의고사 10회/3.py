# 동전 1 - https://www.acmicpc.net/problem/2293
# 재귀, 잘못된 dp - 시간초과

import sys
sys.setrecursionlimit(10000)

N, K = map(int, input().split())
coins = [int(input()) for i in range(N)]
coins.sort()

dp = [[0 for i in range(K + 1)] for j in range(N)]
def use2(prev_idx, val):
    if val == 0:
        return 1
    elif val < 0:
        return 0

    total = 0
    for curr_idx in range(prev_idx, len(coins)):
        total += dp[curr_idx][val - coins[curr_idx]] if dp[curr_idx][val - coins[curr_idx]] else use2(curr_idx, val - coins[curr_idx])

    dp[prev_idx][val] = total
    return total

answer = use2(0, K)
print(answer)