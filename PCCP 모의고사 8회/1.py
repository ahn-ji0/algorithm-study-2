# 거짓말 - https://www.acmicpc.net/problem/1043

from collections import deque

N, M = map(int, input().split())

truth= list(map(int, input().split()))
answer = [1 for i in range(M)]

people = [[] for i in range(N)]

party = []
for i in range(M):
    party.append(list(map(int, input().split())))
    for j in party[-1][1:]:
        people[j-1].append(i)
        
queue = deque()
visited = [0 for i in range(N)]
for i in truth[1:]:
    queue.append(i-1)
    visited[i-1] = 1
    
while queue:
    tmp = queue.popleft()
    
    for p in people[tmp]:
        answer[p] = 0
        for participant in party[p][1:]:
            if not visited[participant-1]:
                visited[participant-1] = 1
                queue.append(participant-1)

print(sum(answer))