#   작성자 : 컴퓨터공학부 최완우
#   작성일 : 2025.11.06

import sys
from collections import deque
input = sys.stdin.readline

N, K = map(int, input().split())
pos_max = 100000
dist = [0] * (pos_max + 1)
visit = [False] * (pos_max + 1)

def bfs() :
    queue = deque([N])
    visit[N] = True
    
    while queue :
        x = queue.popleft()
        if x == K :
            return dist[x]
        
        for nx in [x - 1, x + 1, x * 2] :
            if 0 <= nx <= pos_max and not visit[nx] :
                visit[nx] = True
                dist[nx] = dist[x] + 1
                queue.append(nx)
                
print(bfs())