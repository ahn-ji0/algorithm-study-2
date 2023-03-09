# https://www.acmicpc.net/problem/14888

# 연산자 끼워넣기
def dfs(idx, count, answer):
    global N, arr, cases
    if idx == N:
        cases.append(answer)
        return
    
    for i in range(4):
        if i == 0 and count[i]!=0:
            count[i] -= 1
            dfs(idx + 1, count, answer + arr[idx])
            count[i] += 1
        elif i == 1 and count[i]!=0:
            count[i] -= 1
            dfs(idx + 1, count, answer - arr[idx])
            count[i] += 1
        elif i == 2 and count[i]!=0:
            count[i] -= 1
            dfs(idx + 1, count, answer * arr[idx])
            count[i] += 1
        elif i == 3 and count[i]!=0:
            count[i] -= 1
            dfs(idx + 1, count, int(answer / arr[idx]))
            count[i] += 1
          
N = int(input())


arr = list(map(int,input().split()))
count = list(map(int,input().split()))

cases = []
dfs(1, count, arr[0])    
print(max(cases), min(cases))
