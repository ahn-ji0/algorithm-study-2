# https://www.acmicpc.net/problem/1463

# 나이트의 이동
from collections import deque

dx = [1,2,2,1,-1,-2,-2,-1]
dy = [2,1,-1,-2,-2,-1,1,2]

def bfs(start, destination, visited):
    if start == destination:
        return 0
    queue = deque()
    queue.append((1, start[0], start[1]))
    visited[start[0]][start[1]] = 1
    
    while queue:
        depth, x, y = queue.popleft()
        for i in range(len(dx)):
            tmp_x = x + dx[i]
            tmp_y = y + dy[i]
            if tmp_x < 0 or tmp_x >= N or tmp_y < 0 or tmp_y >= N: continue
            if visited[tmp_x][tmp_y]: continue
            
            visited[tmp_x][tmp_y] = 1
            queue.append((depth+1, tmp_x, tmp_y))
            
            if tmp_x == destination[0] and tmp_y == destination[1]:
                return depth

num_cases = int(input())

for _ in range(num_cases):
    cases = []
    N = int(input())
    start = tuple(map(int,input().split()))
    destination = tuple(map(int,input().split()))
    visited = [[0] * N for _ in range(N)]
    print(bfs(start, destination, visited))