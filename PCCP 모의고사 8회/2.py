# 최소비용 구하기 - https://www.acmicpc.net/problem/1916
# 시간초과 
# 하지만 heapq로 풀어도 시간초과 -> 입력을 sys 사용했더니 해결.

import heapq
import sys

input = sys.stdin.readline

N = int(input())
M = int(input())
INF = 100000 * (N-1) + 1

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

def dijkstra_heapq(N, start, end):
    global graph
    
    distance = [INF for i in range(N)]
    distance[start] = 0
    
    queue = []
    heapq.heappush(queue,(distance[start], start))
    
    while queue:
        tmp_distance, tmp_node = heapq.heappop(queue)
        
        if distance[tmp_node] < tmp_distance:
            continue
        
        for neighbor_node, neighbor_cost in graph[tmp_node]:
            if tmp_distance + neighbor_cost < distance[neighbor_node]:
                distance[neighbor_node] = tmp_distance + neighbor_cost
                heapq.heappush(queue, (tmp_distance + neighbor_cost, neighbor_node))
        
    return distance[end]

graph = [[] for i in range(N)]
for i in range(M):
    tmp_start, tmp_end, tmp_cost = map(int, input().split())
    graph[tmp_start -1].append((tmp_end - 1, tmp_cost))

start, end = map(int, input().split())
print(dijkstra(N, start - 1, end - 1))
    
    