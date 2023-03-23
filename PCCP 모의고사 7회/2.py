# 주유소 - https://www.acmicpc.net/problem/13305

N = int(input())

road = list(map(int, input().split()))
price = list(map(int, input().split()))

stop = []
p = price[0]
stop.append(0)
for i in range(1, N):
    if price[i] < p:
        p = price[i]
        stop.append(i)

total = 0
for i in range(0, len(stop) - 1):
    total += price[stop[i]] * sum(road[stop[i]:stop[i+1]])

total += price[stop[-1]] * sum(road[stop[-1]:])
print(total)