# 회전초밥 - https://www.acmicpc.net/problem/2531

import sys
input = sys.stdin.readline
N, d, k, c = map(int, input().split())

belt = [int(input()) for i in range(N)]

max_val = 0
for idx in range(N):
    new = set()
    for i in range(k):
        curr = belt[(idx + i) % N]
        new.add(curr)

    new.add(c)
    max_val = max(max_val, len(new))

print(max_val)

