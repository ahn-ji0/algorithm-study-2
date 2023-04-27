from collections import deque
n, m = map(int, input().split())
grid = [list(map(int, input().split())) for i in range(n)]

walls = []
for i in range(n):
    for j in range(m):
        if grid[i][j] == 2:
            end_x, end_y = i, j
        elif grid[i][j] == 0:
            walls.append((i,j))

dx = [0,1,0,-1]
dy = [1,0,-1,0]
def bfs(end_x, end_y, walls):
    answer = [[-1 for i in range(m)] for j in range(n)]
    visited = [[False for i in range(m)] for j in range(n)]
    queue = deque([(end_x, end_y)])
    visited[end_x][end_y] = True
    answer[end_x][end_y] = 0
    while queue:
        x, y = queue.popleft()

        for i in range(len(dx)):
            tmp_x, tmp_y = x + dx[i], y + dy[i]
            if tmp_x < 0 or tmp_x >= n or tmp_y < 0 or tmp_y >= m or visited[tmp_x][tmp_y] or grid[tmp_x][tmp_y] == 0:
                continue

            visited[tmp_x][tmp_y] = True
            answer[tmp_x][tmp_y] = answer[x][y] + 1
            queue.append((tmp_x, tmp_y))
    for i, j in walls:
        answer[i][j] = 0
    return answer

answer = bfs(end_x, end_y, walls)
for i in range(len(answer)):
    print(' '.join(str(val) for val in answer[i]))