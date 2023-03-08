# https://school.programmers.co.kr/learn/courses/15009/lessons/121688

import heapq

def solution(ability, number):
    
    heapq.heapify(ability)
    
    for _ in range(number):
        add = heapq.heappop(ability)
        add += heapq.heappop(ability)

        heapq.heappush(ability, add)
        heapq.heappush(ability, add)
    
    return sum(list(ability))

print(solution([10,3,7,2], 2))
print(solution([1,2,3,4],3))