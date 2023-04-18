# 뱀과 사다리 게임 - https://www.acmicpc.net/problem/16928

from collections import deque
N, M = map(int, input().split())
grid = [-1 for i in range(100)]

def bfs():
    visited = [False for i in range(100)]
    queue = deque()
    queue.append((0,0))
    visited[0] = False
    while queue:
        curr, n = queue.popleft()
        for i in range(1, 7):
            tmp_curr = curr + i
            if tmp_curr >= 100:
                continue

            if grid[tmp_curr] != -1:
                tmp_curr = grid[tmp_curr]

            if visited[tmp_curr]:
                continue

            if tmp_curr == 99:
                return n + 1

            queue.append((tmp_curr, n + 1))
            visited[tmp_curr] = True
    return -1

for i in range(N):
    x, y = map(int, input().split())
    grid[x-1] = y-1

for i in range(M):
    u, v = map(int, input().split())
    grid[u-1] = v-1

print(bfs())