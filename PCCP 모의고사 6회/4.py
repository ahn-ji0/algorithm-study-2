# 1012 유기농 배추 - https://www.acmicpc.net/problem/1012

from collections import deque

dx = [0,1, 0, -1]
dy = [1,0,-1,0]

def bfs(x, y):
    global visited, grid
    queue = deque()
    
    queue.append((x,y))
    visited[x][y] = 1
    
    while queue:
        x, y = queue.popleft()
        
        for i in range(len(dx)):
            tmp_x = x + dx[i]
            tmp_y = y + dy[i]
            
            if tmp_x < 0 or tmp_x >= N or tmp_y < 0 or tmp_y >= M or visited[tmp_x][tmp_y]:
                continue
            
            if grid[tmp_x][tmp_y] == 1:
                visited[tmp_x][tmp_y] = 1
                queue.append((tmp_x, tmp_y))

T = int(input())

for _ in range(T):
    M, N, K = map(int, input().split())

    visited = [[0 for i in range(M)] for j in range(N)]

    grid = [[0 for i in range(M)] for j in range(N)]

    for i in range(K):
        x, y = map(int, input().split())
        grid[y][x] = 1

    count = 0
    for i in range(N):
        for j in range(M):
            if grid[i][j] == 1 and not visited[i][j]:
                bfs(i, j)
                count += 1
    
    print(count)

    