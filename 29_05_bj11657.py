#   작성자 : 컴퓨터공학부 최완우
#   작성일 : 2025.11.08

import sys
input = sys.stdin.readline

N, M = map(int, input().split())
edge = []
for _ in range(M) :
    A, B, C = map(int, input().split())
    edge.append((A, B, C))
    
inf = int(1e9)
dist = [inf] * (N + 1)
dist[1] = 0
cycle = False

for i in range(N) :
    for u, v, w in edge :
        if dist[u] != inf and dist[v] > dist[u] + w :
            dist[v] = dist[u] + w
            if i == N - 1 :
                cycle = True
                break

if cycle :
    print(-1)
else :
    for i in range(2, N + 1) :
        print(dist[i] if dist[i] != inf else -1)