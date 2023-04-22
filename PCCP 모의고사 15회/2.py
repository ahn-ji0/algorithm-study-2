# 두 배열의 합 - https://www.acmicpc.net/problem/2143

import sys
input = sys.stdin.readline

T = int(input())
n = int(input())
A = list(map(int, input().split()))
m = int(input())
B = list(map(int, input().split()))

dp_A = [A[0]]
for i in range(1, n):
    dp_A.append(dp_A[-1] + A[i])
dp_B = [B[0]]
for i in range(1, m):
    dp_B.append(dp_B[-1] + B[i])

A_dict = dict()
for i in range(1, n + 1):
    A_dict[dp_A[i-1]] = A_dict[dp_A[i-1]] + 1 if dp_A[i-1] in A_dict else 1
    for j in range(i, n):
        A_dict[dp_A[j] - dp_A[j - i]] = A_dict[dp_A[j] - dp_A[j - i]] + 1 if dp_A[j] - dp_A[j - i] in A_dict else 1

B_dict = dict()
for i in range(1, m + 1):
    B_dict[dp_B[i-1]] = B_dict[dp_B[i-1]] + 1 if dp_B[i-1] in B_dict else 1
    for j in range(i, m):
        B_dict[dp_B[j] - dp_B[j - i]] = B_dict[dp_B[j] - dp_B[j - i]] + 1 if dp_B[j] - dp_B[j - i] in B_dict else 1

total = 0
for a_k in A_dict.keys():
    if T-a_k in B_dict:
        total = total + A_dict[a_k] * B_dict[T-a_k]

print(total)

