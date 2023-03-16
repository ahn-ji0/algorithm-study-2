# 20291 파일정리 https://www.acmicpc.net/problem/20291

N = int(input())

org = dict()
for i in range(N):
    ext = input().split(".")[1]
    if ext not in org: 
        org[ext] = 0
    org[ext] += 1

sorted_org = sorted(org.items())
for key, value in sorted_org:
    print(key, value)