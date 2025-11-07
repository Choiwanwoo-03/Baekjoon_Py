#   작성자 : 컴퓨터공학부 최완우
#   작성일 : 2025.11.07

import heapq
import sys
input = sys.stdin.readline

N, M = map(int, input().split())
graph = [[] for _ in range(N + 1)]
indegree = [0] * (N + 1)
for _ in range(M) :
    a, b = map(int, input().split())
    graph[a].append(b)
    indegree[b] += 1
heap = []
for i in range(1, N + 1) : 
    if indegree[i] == 0 :
        heapq.heappush(heap, i)
result = []
while heap:
    now = heapq.heappop(heap)
    result.append(now)
    for nb in graph[now] :
        indegree[nb] -= 1
        if indegree[nb] == 0:
            heapq.heappush(heap, nb)
print(' '.join(map(str, result)))