# 연속합 - https://www.acmicpc.net/problem/1912
# 구현* - 성공

N = int(input())
arr = list(map(int, input().split()))

total = 0
max_val = max(arr)
for i in range(len(arr)):
    total += arr[i]
    max_val = max(max_val, total)
    if total < 0:
        total = 0

print(max_val)