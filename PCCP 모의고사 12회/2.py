# 파티 - https://www.acmicpc.net/problem/1238
# 플로이드 와샬 - 시간초과

import sys
input = sys.stdin.readline
N, M, X = map(int, input().split())

INF = int(1e9)

distance = [[INF for i in range(N)] for j in range(N)]

for i in range(M):
    start, end, weight = map(int, input().split())
    distance[start-1][end-1] = weight

for i in range(N):
    for j in range(N):
        if i == j:
            distance[i][j] = 0

for k in range(N):
    for i in range(N):
        for j in range(N):
            if distance[i][k] + distance[k][j] < distance[i][j]:
                distance[i][j] = distance[i][k] + distance[k][j]

max_val = 0
for i in range(N):
    val = distance[i][X-1] + distance[X-1][i]
    max_val = max(max_val, val)
print(max_val)