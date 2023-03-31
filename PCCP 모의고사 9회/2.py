# 겉넓이 구하기 - https://www.acmicpc.net/problem/16931

N, M = map(int, input().split())

grid = []
for i in range(N):
    grid.append(list(map(int, input().split())))
    
total = 0

total += 2 * (N * M)

def left():
    total = 0
    for i in range(N):
        total += grid[i][0]
        prev = grid[i][0]
        for j in range(1, M):
            if grid[i][j] > prev:
                total += grid[i][j] - prev
            prev = grid[i][j]
        
    return total

def up():
    total = 0
    for j in range(M):
        total += grid[0][j]
        prev = grid[0][j]
        for i in range(1, N):
            if grid[i][j] > prev:
                total += grid[i][j] - prev
            prev = grid[i][j]
    return total

total += 2 * left()

total += 2 * up()
    
print(total)