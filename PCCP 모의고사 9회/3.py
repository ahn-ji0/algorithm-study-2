# 배열 돌리기 4 - https://www.acmicpc.net/problem/17406

N, M, K= map(int, input().split())

def get_A(arr):
    min_arr = []
    
    for i in range(N):
        min_arr.append(sum(arr[i]))
        
    return min(min_arr)

def rotate(info, grid):
    r, c, s = info
    r -= 1
    c -= 1
    arr = [[0 for i in range(M)] for j in range(N)]
    
    for i in range(N):
        for j in range(M):
            if i < r - s or i > r + s or j < c - s or j > c + s:
                arr[i][j] = grid[i][j]
                continue
    
    arr[r][c] = grid[r][c]
    for loop in range(1, s + 1):
        for j in range(c - loop + 1, c + loop + 1):
            arr[r - loop][j] = grid[r-loop][j-1]

        for i in range(r - loop + 1, r + loop + 1):
            arr[i][c+loop] = grid[i-1][c+loop]
            
        for j in range(c-loop, c+loop):
            arr[r + loop][j] = grid[r+loop][j+1]
        
        for i in range(r-loop, r+loop):
            arr[i][c - loop] = grid[i+1][c-loop]
    
    return arr
                
def dfs(A, visited, depth):
    global info, min_val
    
    if depth == K:
        min_val.append(get_A(A))
        return
    
    for i in range(len(info)):
        if not visited[i]:
            visited[i] = 1
            dfs(rotate(info[i], A), visited, depth + 1)
            visited[i] = 0
    
A = []
for i in range(N):
    A.append(list(map(int, input().split())))

info = []
for i in range(K):
    info.append(tuple(map(int, input().split())))

visited = [0 for i in range(K)]
min_val = []
dfs(A, visited, 0)

print(min(min_val))