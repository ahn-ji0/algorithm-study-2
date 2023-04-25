# 트럭 - https://www.acmicpc.net/problem/13335

from collections import deque
n, w, L = map(int, input().split())
a = deque(map(int, input().split()))

queue = deque()
time = 0
total = 0
while True:
    if len(queue) == w:
        val = queue.popleft()
        if val:
            total += 1

    if total == n:
        time += 1
        break

    if not a:
        queue.append(0)
        time += 1
        continue

    curr = a[0]
    if sum(queue) + curr > L:
        queue.append(0)
        time += 1
        continue

    queue.append(a.popleft())
    time += 1

print(time)