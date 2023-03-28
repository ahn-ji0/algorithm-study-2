# A -> B - https://www.acmicpc.net/problem/16953

import heapq

def bfs(A, B):
    depth = 0
    queue = []
    heapq.heappush(queue,(A, 0))
    while queue:
        x, depth =heapq.heappop(queue)
        if x > B:
            return -2
        for num in [x * 2, 10 * x + 1]:

            if num == B:
                return depth + 1
            
            heapq.heappush(queue, (num, depth + 1))

A, B = map(int, input().split())

print(bfs(A, B) + 1)