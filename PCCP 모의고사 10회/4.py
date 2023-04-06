# 여행 가자 - https://www.acmicpc.net/problem/1976

from collections import  deque
N = int(input())
M = int(input())
graph = [list(map(int, input().split())) for i in range(N)]
plan = list(map(int, input().split()))

for i in range(len(plan)):
    plan[i] -= 1

def bfs(start):
    queue = deque()
    queue.append(start)
    visited[start] = 1
    while queue:
        curr = queue.popleft()
        for i in range(N):
            # print(curr, i)
            # print(visited)
            # print(graph)
            if not visited[i] and graph[curr][i]:
                visited[i] = 1
                queue.append(i)

    return

visited = [0 for i in range(N)]
bfs(plan[0])

answer = True
for i in range(len(plan)):
    if not visited[plan[i]]:
        answer = False
        break

if answer:
    print("YES")
else:
    print("NO")


