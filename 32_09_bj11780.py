#   작성자 : 컴퓨터공학부 최완우
#   작성일 : 2025.11.12

import sys
input = sys.stdin.readline

def get_route(start, end, path, route):
    if path[start][end] == 0:
        route.append(start)
        return

    mid = path[start][end]
    get_route(start, mid, path, route)
    get_route(mid, end, path, route)


def solve():
    try:
        N = int(input())
        M = int(input())
    except:
        return

    INF = int(1e9)
    dist = [[INF] * (N + 1) for _ in range(N + 1)]
    path = [[0] * (N + 1) for _ in range(N + 1)]
    
    for i in range(1, N + 1):
        dist[i][i] = 0

    for _ in range(M):
        a, b, c = map(int, input().split())
        dist[a][b] = min(dist[a][b], c)

    for k in range(1, N + 1):
        for i in range(1, N + 1):
            for j in range(1, N + 1):
                if dist[i][j] > dist[i][k] + dist[k][j]:
                    dist[i][j] = dist[i][k] + dist[k][j]
                    path[i][j] = k

    for i in range(1, N + 1):
        for j in range(1, N + 1):
            if dist[i][j] == INF:
                print(0, end=" ")
            else:
                print(dist[i][j], end=" ")
        print()

    for i in range(1, N + 1):
        for j in range(1, N + 1):
            route = []
            
            if dist[i][j] == 0 or dist[i][j] == INF:
                print(0)
            else:
                get_route(i, j, path, route)
                
                route.append(j) 
                
                print(len(route), *route)

solve()