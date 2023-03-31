# 퇴사 2 - https://www.acmicpc.net/problem/15486

import heapq
import sys

input = sys.stdin.readline

N = int(input())

time = []
profit = []

for i in range(N):
    t, p = map(int, input().split())
    time.append(t)
    profit.append(p)

# # dp[i] 는 i 날 상담했을 때 최대로 벌 수 있는 금액
# dp = [0 for i in range(N)]
# max_dp = []
# for i in range(N-1, -1, -1):
#     if i + time[i] > N:
#         continue
    
#     dp[i] =  profit[i]
#     if i + time[i] < N:
#         dp[i] += max(dp[i + time[i]:])


# dp[i] 는 i일 이후에 최대로 벌 수 있는 금액
max_val = 0
dp = [0 for i in range(N)]
max_dp = []
for i in range(N-1, -1, -1):
    if i + time[i] > N:
        dp[i] = max_val
        continue
        
    curr_val = 0
    if i + time[i] == N:
        curr_val = profit[i]
    else: curr_val = profit[i] + dp[i + time[i]]
    
    if curr_val > max_val:
        dp[i] = curr_val
        max_val = dp[i]
    else:
        dp[i] = max_val
        
print(dp[0])