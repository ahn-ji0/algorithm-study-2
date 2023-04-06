# 유기농 배추 - https://www.acmicpc.net/problem/1012

from collections import deque
T = int(input())
di = [1,0,-1,0]
dj = [0,1,0,-1]
def bfs(i, j, grid):
    queue = deque()
    queue.append((i,j))
    visited[i][j] = 1
    while queue:
        # print(queue)
        i, j = queue.popleft()
        for a in range(len(di)):
            tmp_i = i + di[a]
            tmp_j = j + dj[a]
            if tmp_i < 0 or tmp_i >= N or tmp_j < 0 or tmp_j >= M:
                continue

            if visited[tmp_i][tmp_j] or not grid[tmp_i][tmp_j]:
                continue

            visited[tmp_i][tmp_j] = 1
            queue.append((tmp_i, tmp_j))

for t in range(T):
    M, N, K = map(int, input().split())
    grid = [[0 for i in range(M)] for j in range(N)]
    for i in range(K):
        y, x = map(int, input().split())
        grid[x][y] = 1
    # print(grid)

    cnt = 0
    visited = [[0 for i in range(M)] for j in range(N)]
    for i in range(N):
        for j in range(M):
            if not visited[i][j] and grid[i][j]:
                # print('hi')
                bfs(i,j, grid)
                cnt += 1

    print(cnt)

