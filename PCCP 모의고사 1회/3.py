# 유전법칙 - https://school.programmers.co.kr/learn/courses/15008/lessons/121685
# 재귀

sequence = ['RR', 'Rr', 'Rr', 'rr']

def get_characteristics(gen, seq):
    if gen == 1:
        return 'Rr'
    if gen == 2:
        return sequence[seq]
    
    parent = get_characteristics(gen-1, seq//4)
    if parent == 'RR':
        return 'RR'
    elif parent == 'rr':
        return 'rr'
    else:
        return sequence[seq % 4]

def solution(queries):
    answer = []

    for q in queries:
        answer.append(get_characteristics(q[0], q[1]-1))
    
    return answer

print(solution([[3,5]]))
print(solution([[3, 8], [2, 2]]))
print(solution([[3, 1], [2, 3], [3, 9]]))
print(solution([[4, 26]]))