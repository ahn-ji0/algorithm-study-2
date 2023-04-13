# 부등호 - https://www.acmicpc.net/problem/2529

k = int(input())
signs = list(input().split())

def success(nums):
    for i in range(1, len(nums)):
        sign = signs[i-1]
        if sign == '<':
            if nums[i-1] > nums[i]:
                return False
        else:
            if nums[i-1] < nums[i]:
                return False

    return True

def dfs(n, visited, nums):
    global min_val, max_val

    if len(nums) == k + 1:
        if success(nums):
            val = ''.join(str(n) for n in nums)
            min_val = min(min_val, val)
            max_val = max(max_val, val)
        return

    for i in range(10):
        if not visited[i]:
            if n == 0:
                visited[i] = 1
                dfs(n + 1, visited, nums + [i])
                visited[i] = 0
            else:
                if signs[n - 1] == '>':
                    if nums[-1] > i:
                        visited[i] = 1
                        dfs(n + 1, visited, nums + [i])
                        visited[i] = 0
                else:
                    if nums[-1] < i:
                        visited[i] = 1
                        dfs(n + 1, visited, nums + [i])
                        visited[i] = 0


visited = [0 for i in range(10)]
min_val = '9999999999'
max_val = '0'
dfs(0, visited, [])
print(max_val)
print(min_val)

