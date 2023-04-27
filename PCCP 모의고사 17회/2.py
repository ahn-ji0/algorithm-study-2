from collections import defaultdict
N = int(input())
cards = list(map(int, input().split()))
M = int(input())
nums = list(map(int, input().split()))

cases = defaultdict(int)
for i in range(N):
    cases[cards[i]] += 1

for j in range(M):
    print(cases[nums[j]], end = ' ')