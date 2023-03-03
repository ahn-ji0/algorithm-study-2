# 체육대회 - https://school.programmers.co.kr/learn/courses/15008/lessons/121684
# premutation / DFS

from itertools import permutations

def solution(ability):
    answer = 0
    num_students = len(ability)
    num_categories = len(ability[0])
    l = list(range(num_students))
    
    max_ability = 0
    for p in permutations(l, num_categories):
        sum = 0
        for category, student in enumerate(p):
            sum += ability[student][category]
        if sum >= max_ability:
            max_ability = sum
    return max_ability

print(solution([[40, 10, 10], [20, 5, 0], [30, 30, 30], [70, 0, 70], [100, 100, 100]]))