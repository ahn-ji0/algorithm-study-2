# 탑 - https://www.acmicpc.net/problem/2493

import heapq
import sys
input = sys.stdin.readline

N = int(input())
arr = list(map(int, input().split()))

answer = [0 for i in range(N)]
queue = []
for curr in range(N-1, -1, -1):
    while queue:
        if queue[0][0] < arr[curr]:
            height, idx = heapq.heappop(queue)
            answer[idx] = curr + 1
        else:
            break
    heapq.heappush(queue, (arr[curr], curr))

print(' '.join([str(x) for x in answer]))