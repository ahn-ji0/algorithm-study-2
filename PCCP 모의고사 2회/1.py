# https://school.programmers.co.kr/learn/courses/15009/lessons/121687

# 북 동 남 서
direction = [[(0,1),(0,-1)], [(1,0),(-1,0)], [(0,-1), (0,1)], [(-1,0),(1,0)]]

def solution(command):
    answer = []
    dir = 0
    x,y = (0,0)
    
    for i in command:
        if i == "G":
            x += direction[dir][0][0]
            y += direction[dir][0][1]
        elif i == "B":
            x += direction[dir][1][0]
            y += direction[dir][1][1]
        elif i == "R":
            dir = (dir+1) % 4
        else:
            dir = (dir-1) % 4
    answer.extend([x,y])
    return answer

print(solution("GRGLGRG"))
print(solution("GRGRGRB"))