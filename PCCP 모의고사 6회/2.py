# 1764 듣보잡 - https://www.acmicpc.net/problem/1764

N, M = map(int, input().split())

n_list = dict()
for _ in range(N):
    n_list[(input())] = 1
    
    
inter = []
for _ in range(M):
    tmp = input()
    if tmp in n_list:
        inter.append(tmp)
        
print(len(inter))
for word in sorted(inter):
    print(word)