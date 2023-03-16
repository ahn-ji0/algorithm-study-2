# 21608 상어 초등학교 - https://www.acmicpc.net/problem/21608

import heapq

N = int(input())
surveys = []
for i in range(N * N):
    surveys.append(list(map(int, input().split())))
    
std = dict()
    
fixed = [[0] * (N) for _ in range(N)]
grid_info = [[[0]] * N for _ in range(N)]
empty_info = [[4] * N for _ in range(N)]
for i in range(N):
    for j in range(N):
        if (i,j) == (0,0) or (i,j) == (0,N-1) or (i,j) == (N-1,0) or (i,j) == (N-1, N-1):
            empty_info[i][j] = 2
        if i == 0 or j == 0 or i == N-1 or j == N-1:
            empty_info[i][j] = 3
empty_info[0][0] = 2
empty_info[0][N-1] = 2
empty_info[N-1][0] = 2
empty_info[N-1][N-1] = 2


for survey in surveys:
    student = survey[0]
    likes = survey[1:]
    std[student] = likes
    
    queue = []
    for i in range(N):
        for j in range(N):
            if fixed[i][j]:
                continue
            
            count = 0
            
            first = N - 1 - len(set(grid_info[i][j]) & set(likes))
            second = 4 - empty_info[i][j]
            third_row = i
            third_col = j
            heapq.heappush(queue, (first,second,third_row,third_col))
    
    _ , _ , x, y = heapq.heappop(queue)
    fixed[x][y] = student
    
    #주변에 알리기, empty 업데이트
    for tmp_x, tmp_y in [(x-1,y), (x+1,y), (x,y+1), (x,y-1)]:
        if tmp_x < 0 or tmp_x >= N or tmp_y < 0 or tmp_y >= N:
            continue
        if grid_info[tmp_x][tmp_y] == [0]:
            grid_info[tmp_x][tmp_y] = [student]
        else:
            grid_info[tmp_x][tmp_y].append(student)
        empty_info[tmp_x][tmp_y] -= 1

total = 0
for x in range(N):
    for y in range(N):
        student = fixed[x][y]
        count = 0
        for tmp_x, tmp_y in [(x-1,y), (x+1,y), (x,y+1), (x,y-1)]:
            if tmp_x < 0 or tmp_x >= N or tmp_y < 0 or tmp_y >= N:
                continue
            if fixed[tmp_x][tmp_y] in std[student]:
                count += 1
                
        if count > 0:
            total += 10 ** (count-1)
        
print(total)