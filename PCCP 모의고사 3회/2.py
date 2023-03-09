# https://school.programmers.co.kr/learn/courses/30/lessons/17681

# 비밀지도
def make_binary(n, num, r):
    if num < 2:
        bin = str(num) + r
        if len(bin) < n:
            bin = '0' * (n-len(bin)) + bin
        return bin
    
    r = str(num % 2) + r
    return make_binary(n, num//2, r)

def re(n, icon):
    if len(icon) == n:
        return icon
    
    return " " * (n-len(icon)) + icon
def solution(n, arr1, arr2):
    answer = []
        
    for i in range(n):
        icon = str(bin(arr1[i] | arr2[i])).lstrip('0b').replace("0"," ").replace("1","#")
        
        answer.append(re(n,icon))
    return answer

print(solution(5,[9, 20, 28, 18, 11], [30, 1, 21, 17, 28]))

# print(solution(6,[46, 33, 33 ,22, 31, 50], [27 ,56, 19, 14, 14, 10]))


