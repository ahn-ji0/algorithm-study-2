# 1890 점프 - https://www.acmicpc.net/problem/1890

dx = [1,0]
dy = [0,1]

def dfs(x,y):
    global dp, grid
    
    total = 0
    if grid[x][y] == 0:
        dp[x][y] = 0
        return 0
    
    for i in range(len(dx)):
        tmp_x = x + grid[x][y] * dx[i]
        tmp_y = y + grid[x][y] * dy[i]
        
        if tmp_x < 0 or tmp_x >= N or tmp_y < 0 or tmp_y >= N:
            continue
        
        if dp[tmp_x][tmp_y]:
            total += dp[tmp_x][tmp_y]
        else:
            total += dfs(tmp_x, tmp_y)
            
    dp[x][y] = total
    return total

N = int(input())

grid = []
for _ in range(N):
    grid.append(list(map(int, input().split())))

dp = [[0 for i in range(N)] for j in range(N)]
dp[N-1][N-1] = 1

print(dfs(0,0))