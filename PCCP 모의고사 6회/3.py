# 14503 로봇 청소기 - https://www.acmicpc.net/problem/14503

# 북 동 남 서 
dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]

def clean(x, y, dir):
    global grid, cln
    
    if grid[x][y] == 0:
        grid[x][y] = 2
        cln += 1
    
    all_cleaned = True
    for i in range(len(dx)):
        tmp_x = x + dx[i]
        tmp_y = y + dy[i]
        
        if tmp_x < 0 or tmp_x >= N or tmp_y < 0 or tmp_y >= M:
            continue
        
        if grid[tmp_x][tmp_y] == 0:
            all_cleaned = False
    
    if not all_cleaned:
        for i in range(len(dx)):
            dir = (dir-1) % 4
            f_x = x + dx[dir]
            f_y = y + dy[dir]

            if f_x <0 or f_x >= N or f_y <0 or f_y >=M or grid[f_x][f_y] == 1:
                continue
            
            if grid[f_x][f_y] == 0:
                return clean(f_x, f_y, dir)
    else:
        b_x = x - dx[dir]
        b_y = y - dy[dir]
        
        if b_x < 0 or b_x >= N or b_y < 0 or b_y >= M or grid[b_x][b_y] == 1:
            return 
        else:
            return clean(b_x, b_y, dir)

N, M = map(int, input().split())
r, c, d = map(int, input().split())

grid = []
for _ in range(N):
    grid.append(list(map(int, input().split())))
cln = 0

clean(r, c, d)
print(cln)