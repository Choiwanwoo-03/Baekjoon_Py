#   작성자 : 컴퓨터공학부 최완우
#   작성일 : 2025.11.08

import sys
import heapq
input = sys.stdin.readline

V, E = map(int, input().split())
K = int(input())
graph = [[] for _ in range(V + 1)]
for _ in range(E) :
    u, v, w = map(int, input().split())
    graph[u].append((v, w))
    
distance = [float('inf')] * (V + 1)
distance[K] = 0

heap = []
heapq.heappush(heap, (0, K))

while heap :
    cur_dist, cur = heapq.heappop(heap)
    if distance[cur] < cur_dist :
        continue
    for next_node, edge_weight in graph[cur] :
        new_dist = cur_dist + edge_weight
        if new_dist < distance[next_node] :
            distance[next_node] = new_dist
            heapq.heappush(heap, (new_dist, next_node))
            
for i in range(1, V + 1) :
    print(distance[i] if distance[i] != float('inf') else "INF")