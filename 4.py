# https://www.acmicpc.net/problem/1463

# recursion 사용 시 런타임 에러 - RecursionError 
# 따라서 반복문으로 변경

def recursion(x):    
    global dp
    
    if x == 1:
        return 0 
    
    case = []
    if x % 3 == 0:
        case.append(recursion(x // 3) + 1 if dp[x] == -1 else dp[x//3] + 1)
    if x % 2 == 0:
        case.append(recursion(x // 2) + 1 if dp[x] == -1 else dp[x//2] + 1)
    case.append(recursion(x-1) + 1 if dp[x] == -1 else dp[x-1] + 1)
    dp[x] = min(case)
    return dp[x]

def iterate(x):
    global dp
    dp[1] = 0
    for i in range(1, N + 1):
        if i + 1 < N + 1:
            dp[i + 1] = min(dp[i + 1], dp[i] + 1)
        if i * 2 < N + 1:
            dp[i * 2] = min(dp[i * 2], dp[i] + 1)
        if i * 3 < N + 1:
            dp[i * 3] = min(dp[i * 3], dp[i] + 1)
    
    return dp[x]

N = int(input())
dp = [1000000] * (N+1)
print(iterate(N))