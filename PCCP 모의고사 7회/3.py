# 연결 요소의 개수 - https://www.acmicpc.net/problem/11724

from collections import deque
import sys

def bfs(node):
    global visited, graph
    
    queue = deque()
    visited[node] = 1
    queue.append(node)
    while queue:
        curr = queue.popleft()
        
        for i in graph[curr]:
            if not visited[i] :
                visited[i] = 1
                queue.append(i)
    
    return

N, M = map(int, sys.stdin.readline().split())
    
# graph = [[0 for i in range(N)] for j in range(N)]
visited = [0 for i in range(N)]

graph = dict()

for i in range(N):
    graph[i] = list()

for _ in range(M):
    x, y = map(int, sys.stdin.readline().split())
    graph[x-1].append(y-1)
    graph[y-1].append(x-1)

count = 0
for i in range(N):
    if not visited[i]:
        bfs(i)
        count+=1

print(count)