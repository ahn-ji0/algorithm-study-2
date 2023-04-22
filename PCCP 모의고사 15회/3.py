# 안녕 - https://www.acmicpc.net/problem/1535

import sys
input = sys.stdin.readline
N = int(input())
L = list(map(int, input().split()))
J = list(map(int, input().split()))

def dfs(lost, prev_joy, prev, joy, visited):
    global max_joy

    if lost <= 0:
        max_joy = max(max_joy, prev_joy)
        return

    for i in range(prev + 1, len(visited)):
        if not visited[i]:
            visited[i] = 1
            dfs(lost - L[i], joy, i, joy + J[i], visited)
            visited[i] = 0

    max_joy = max(max_joy, joy)

max_joy = 0
visited = [0 for i in range(N)]
if sum(L) < 100:
    print(sum(J))
else:
    dfs(100, 0, -1, 0, visited)
    print(max_joy)
