#   작성자 : 컴퓨터공학부 최완우
#   작성일 : 2025.11.12

from collections import deque
import sys
input = sys.stdin.readline

data = input().split()
if not data :
    exit()
    
N = int(data[0])
K = int(data[1])

MAX = 100001
parent = [-1] * MAX
time = [-1] * MAX

def solve(start, end) :
    if start == end :
        return 0
    
    queue = deque([start])
    time[start] = 0
    
    while queue :
        current = queue.popleft()
        
        for next_pos in (current - 1, current + 1, current * 2) :
            if 0 <= next_pos < MAX and time[next_pos] == -1 :
                time[next_pos] = time[current] + 1
                parent[next_pos] = current
                if next_pos == end :
                    return time[end]
                queue.append(next_pos)
    return -1

min_time = solve(N, K)
print(min_time)

route = []
current = K

while current != N :
    route.append(current)
    current = parent[current]
    
route.append(N)
print(*(route[::-1]))