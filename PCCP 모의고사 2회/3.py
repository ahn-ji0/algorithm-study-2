# https://school.programmers.co.kr/learn/courses/15009/lessons/121689

def solution(menu, order, k):
    
    num_customer = len(order)
    exit_time = 0
    exit_idx = -1
    max_count = 0
    for i in range(num_customer):
        if i!= 0 and exit_time < k * i:
            exit_time = k * i + menu[order[i]]
        else:
            exit_time += menu[order[i]]
        count = 0
        for j in range(exit_idx+1, num_customer):
            if k * j < exit_time:
                count += 1
            else: break
                    
        if count > max_count:
            max_count = count
            
        exit_idx = i
        
    return max_count

print(solution([5,12,30],[1,2,0,1],10))
print(solution([5,12,30],[2,1,0,0,0,1,0],10))
print(solution([5],[0,0,0,0,0],5))