# 최소비용 구하기 - https://www.acmicpc.net/problem/1916
# 시간초과

N = int(input())
M = int(input())
INF = 1000 * (N-1) + 1

def find_min(distance, visited):
    min_distance = INF
    min_idx = -1
    for i in range(len(visited)):
        if not visited[i] and distance[i] <= min_distance:
            min_distance = distance[i]
            min_idx = i
    
    return min_idx

def dijkstra(N, start, end):
    global graph
    if start == end:
        return 0
    
    distance = [INF for i in range(N)]
    visited = [False for i in range(N)]
    
    visited[start] = True
    distance[start] = 0
    for neighbor_idx, cost in graph[start]:
        if cost < distance[neighbor_idx]: 
            distance[neighbor_idx] = cost
    
    for _ in range(N-1):
        min_idx = find_min(distance, visited)

        visited[min_idx] = True
        for neighbor_idx, cost in graph[min_idx]:
            if not visited[neighbor_idx] and distance[min_idx] + cost < distance[neighbor_idx]:
                distance[neighbor_idx] = distance[min_idx] + cost
    
    # print(distance)
    return distance[end]

graph = [[] for i in range(N)]
for i in range(M):
    tmp_start, tmp_end, tmp_cost = map(int, input().split())
    graph[tmp_start -1].append((tmp_end - 1, tmp_cost))

start, end = map(int, input().split())
print(dijkstra(N, start - 1, end - 1))
    
    