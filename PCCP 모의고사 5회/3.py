# 숨바꼭질 3 - https://www.acmicpc.net/problem/13549

import heapq

def bfs(start, end):
    if start == end:
        return 0
    
    visited = [0] * 100001
    queue = []
    
    heapq.heappush(queue, (0, start))
    visited[start] = 1
    
    total_time = 0
    stop = False
    while not stop:
        curr_time, loc = heapq.heappop(queue)
        
        for tmp_loc, time in [(loc * 2, 0), (loc + 1, 1),(loc - 1, 1)]:
            if tmp_loc < 0 or tmp_loc > 100000 or visited[tmp_loc]:
                continue
            
            if tmp_loc == end:
                total_time = curr_time + time
                stop = True
                break
            
            visited[tmp_loc] = 1
            heapq.heappush(queue, (curr_time + time, tmp_loc))
            
    return total_time
            
N, K = map(int, input().split())
print(bfs(N, K))