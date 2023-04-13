# 미세먼지 안녕! - https://www.acmicpc.net/problem/17144

import sys
input = sys.stdin.readline

R, C, T = map(int, input().split())
A = [list(map(int, input().split())) for i in range(R)]
cleaner = -1
for i in range(R):
    if A[i][0] == -1:
        cleaner = i
        break

dx = [0, 1, 0, -1]
dy = [1, 0, -1, 0]

for t in range(T):
    # 미세먼지 확산
    added = [[0 for i in range(C)] for j in range(R)]
    for x in range(R):
        for y in range(C):
            if A[x][y] == 0 or A[x][y] == -1:
                continue
            cnt = 0
            for i in range(len(dx)):
                tmp_x, tmp_y = x + dx[i], y + dy[i]
                if tmp_x < 0 or tmp_x >= R or tmp_y < 0 or tmp_y >= C or A[tmp_x][tmp_y] == -1:
                    continue

                cnt += 1
                added[tmp_x][tmp_y] += A[x][y] // 5

            A[x][y] -= (A[x][y] // 5) * cnt ## 다시
    for x in range(R):
        for y in range(C):
            A[x][y] += added[x][y]

    # 공기청정기 작동
    # 위
    prev = A[0][1]
    for i in range(0, cleaner + 1):
        curr = A[i][0]
        A[i][0] = prev
        prev = curr

    for j in range(1, C):
        curr = A[cleaner][j]
        A[cleaner][j] = prev
        prev = curr

    for i in range(cleaner - 1, -1, -1):
        curr = A[i][C-1]
        A[i][C-1] = prev
        prev = curr

    for j in range(C-2, -1, -1):
        curr = A[0][j]
        A[0][j] = prev
        prev = curr
    A[cleaner][0] = -1
    A[cleaner][1] = 0

    # 아래
    prev = A[cleaner + 2][0]
    for j in range(0, C):
        curr = A[cleaner + 1][j]
        A[cleaner + 1][j] = prev
        prev = curr
    for i in range(cleaner + 2, R):
        curr = A[i][C-1]
        A[i][C - 1] = prev
        prev = curr
    for j in range(C-2, -1 ,-1):
        curr = A[R-1][j]
        A[R - 1][j] = prev
        prev = curr
    for i in range(R-2, cleaner, -1):
        curr = A[i][0]
        A[i][0] = prev
        prev = curr
    A[cleaner + 1][0] = -1
    A[cleaner + 1][1] = 0


total = 0
for i in range(R):
    for j in range(C):
        if A[i][j] != -1:
            total += A[i][j]
print(total)