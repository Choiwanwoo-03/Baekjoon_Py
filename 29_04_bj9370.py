#   작성자 : 컴퓨터공학부 최완우
#   작성일 : 2025.11.08

import sys
import heapq
input = sys.stdin.readline

inf = int(1e9)

def solve(start, n, graph) :
    distance = [inf] * (n + 1)
    distance[start] = 0
    q = [(0, start)]
    while q :
        cost, now = heapq.heappop(q)
        if cost > distance[now] :
            continue
        for nxt, w in graph[now] :
            if distance[nxt] > cost + w :
                distance[nxt] = cost + w
                heapq.heappush(q, (distance[nxt], nxt))
    return distance

T = int(input())
for _ in range(T) :
    n, m, t = map(int, input().split())
    s, g, h = map(int, input().split())
    graph = [[] for _ in range(n + 1)]
    for _ in range(m) :
        a, b, d = map(int, input().split())
        graph[a].append((b, d))
        graph[b].append((a, d))
    destination = [int(input()) for _ in range(t)]
    
    dist_s = solve(s, n, graph)
    dist_g = solve(g, n, graph)
    dist_h = solve(h, n, graph)
    
    answer = []
    for i in sorted(destination) :
        route1 = dist_s[g] + dist_g[h] + dist_h[i]
        route2 = dist_s[h] + dist_h[g] + dist_g[i]
        if dist_s[i] == route1 or dist_s[i] == route2 :
            answer.append(i)
    print(*answer)