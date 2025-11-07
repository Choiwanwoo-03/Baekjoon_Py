#   작성자 : 컴퓨터공학부 최완우
#   작성일 : 2025.11.07

from collections import deque
import sys
input = sys.stdin.readline

N, M = map(int, input().split())
graph = [[] for _ in range(N + 1)]
indegree = [0] * (N + 1)
for _ in range(M) :
    a, b = map(int, input().split())
    graph[a].append(b)
    indegree[b] += 1
    
queue = deque()
for i in range(1, N + 1) :
    if indegree[i] == 0 :
        queue.append(i)
        
answer = []
while queue :
    current = queue.popleft()
    answer.append(current)
    for i in graph[current] :
        indegree[i] -= 1
        if indegree[i] == 0 :
            queue.append(i)
print(' '.join(map(str, answer)))