# 색종이 - https://www.acmicpc.net/problem/2563

N = int(input())

papers = []
for i in range(N):
    papers.append(tuple(map(int, input().split())))

total = [[0 for i in range(100)] for j in range(100)]
for paper in papers:
    x, y = paper
    for i in range(10):
        for j in range(10):
            total[x+i][y+j] = 1

answer = 0
for i in range(100):
    answer += sum(total[i])
    
print(answer)