import sys
import heapq

input = sys.stdin.readline
N, M, X = map(int, input().split())

INF = int(1e9)

road = [[] for i in range(N)]

for i in range(M):
    start, end, weight = map(int, input().split())
    road[start-1].append((end-1, weight))


def dijkstra(start):
    distance = [INF for i in range(N)]
    distance[start] = 0
    queue = []
    heapq.heappush(queue, (0, start))
    while queue:
        dist, curr = heapq.heappop(queue)

        if dist > distance[curr]:
            continue

        for n_idx, n_weight in road[curr]:
            if dist + n_weight < distance[n_idx]:
                distance[n_idx] = dist + n_weight
                heapq.heappush(queue, (distance[n_idx], n_idx))
    return distance

dijkstras = []
for i in range(N):
    dijkstras.append(dijkstra(i))

max_total = 0
for i in range(N):
    total = dijkstras[i][X-1] + dijkstras[X-1][i]
    max_total = max(max_total, total)
print(max_total)


