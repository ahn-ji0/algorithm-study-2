from collections import defaultdict, deque
g, N = map(int, input().split())
W = input().rstrip()
S = input().rstrip()

w_dict = defaultdict(int)
for i in range(g):
    w_dict[W[i]] += 1

result = list()
queue = deque()
for i in range(N):

    if len(queue) == g:
        result.append(''.join(list(queue)))
        pop_idx = queue.popleft()
        w_dict[pop_idx] += 1

    if S[i] in w_dict and w_dict[S[i]] >= 1:
        w_dict[S[i]] -= 1
        queue.append(S[i])
    elif S[i] not in w_dict:
        while queue:
            tmp = queue.popleft()
            w_dict[tmp] += 1
    else:
        while w_dict[S[i]] < 1:
            tmp = queue.popleft()
            w_dict[tmp] += 1
        w_dict[S[i]] -= 1
        queue.append(S[i])

if len(queue) == g:
    result.append(''.join(list(queue)))

# print(result)
print(len(result))