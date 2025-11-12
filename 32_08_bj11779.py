#   작성자 : 컴퓨터공학부 최완우
#   작성일 : 2025.11.12

import sys
import heapq

input = sys.stdin.readline

def solve():
    try:
        N = int(input())
        M = int(input())
    except:
        return

    graph = [[] for _ in range(N + 1)]
    for _ in range(M):
        start, end, cost = map(int, input().split())
        graph[start].append((end, cost))

    start_city, end_city = map(int, input().split())

    INF = int(1e9)
    distance = [INF] * (N + 1)
    path_tracker = [0] * (N + 1)
    
    pq = []
    
    distance[start_city] = 0
    heapq.heappush(pq, (0, start_city))

    while pq:
        cost, now = heapq.heappop(pq)

        if distance[now] < cost:
            continue

        for next_node, next_cost in graph[now]:
            new_cost = cost + next_cost
            
            if new_cost < distance[next_node]:
                distance[next_node] = new_cost
                path_tracker[next_node] = now
                heapq.heappush(pq, (new_cost, next_node))

    min_cost = distance[end_city]
    print(min_cost)

    route = []
    current_node = end_city
    while current_node != 0:
        route.append(current_node)
        current_node = path_tracker[current_node]

    route.reverse()
    
    print(len(route))
    print(*route)

if __name__ == "__main__":
    solve()