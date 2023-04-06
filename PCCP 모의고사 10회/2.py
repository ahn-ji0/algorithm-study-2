# 연속합 - https://www.acmicpc.net/problem/1912
# dp, combination - 시간초과

N = int(input())
arr = list(map(int, input().split()))

dp = [0 for i in range(N)]

dp[0] = arr[0]
for i in range(1, N):
    dp[i] = dp[i - 1] + arr[i]

def combinations(arr, n):
    result = []

    if n == 0:
        return [[]]

    for i in range(len(arr)):
        element = arr[i]
        for next in combinations(arr[i+1:], n - 1):
            result.append([element] + next)

    return result

max_val = max(arr)
for combi in combinations(dp, 2):
    max_val = max(max_val, combi[1] - combi[0])

print(max_val)