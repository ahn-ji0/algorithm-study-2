# 외톨이 알파벳 - https://school.programmers.co.kr/learn/courses/15008/lessons/121683
# 문자열

from collections import defaultdict

def solution(input_string):
    compact = list()
    alphabet = set(input_string)
    compact.append(input_string[0])
    for i in range(1, len(input_string)):
        if input_string[i] != compact[-1]:
            compact.append(input_string[i])
    
    compact.sort()
    
    answer = ''
    
    for i in alphabet:
        if compact.count(i) >= 2:
            answer += i
    if answer == '': 
        return "N"
    return ''.join(sorted(answer))
    
print(solution("edeaaabbccd"))
print(solution("eeddee"))
print(solution("string"))
print(solution("zbzbz"))