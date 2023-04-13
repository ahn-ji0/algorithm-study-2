# 에너지 모으기 - https://www.acmicpc.net/problem/16198

N = int(input())
weight = list(map(int, input().split()))

def dfs(arr, energy):
    global max_energy

    if len(arr) == 2:
        max_energy = max(max_energy, energy)
        return

    for i in range(1, len(arr) - 1):
        dfs(arr[:i] + arr[i+1:], energy + arr[i-1] * arr[i+1])


visited = [0 for i in range(N-2)]

max_energy = 0
dfs(weight, 0)
print(max_energy)