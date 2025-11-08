#   작성자 : 컴퓨터공학부 최완우
#   작성일 : 2025.11.08

import sys
import heapq
input = sys.stdin.readline

inf = int(1e9)
N, E = map(int, input().split())
graph = [[] for _ in range(N + 1)]

for _ in range(E) :
    a, b, c = map(int, input().split())
    graph[a].append((b, c))
    graph[b].append((a, c))
    
v1, v2 = map(int, input().split())

def solve(start) :
    distance = [inf] * (N + 1)
    distance[start] = 0
    heap = [(0, start)]
    
    while heap :
        dist, node = heapq.heappop(heap)
        if dist > distance[node] :
            continue
        for nxt, w in graph[node] :
            cost = dist + w
            if cost < distance[nxt] :
                distance[nxt] = cost
                heapq.heappush(heap, (cost, nxt))
    return distance

dist_from_1 = solve(1)
dist_from_v1 = solve(v1)
dist_from_v2 = solve(v2)

route1 = dist_from_1[v1] + dist_from_v1[v2] + dist_from_v2[N]
route2 = dist_from_1[v2] + dist_from_v2[v1] + dist_from_v1[N]

result = min(route1, route2)

if result >= inf :
    print(-1)
else :
    print(result)