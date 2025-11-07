#   작성자 : 컴퓨터공학부 최완우
#   작성일 : 2025.11.07

import sys
from collections import deque
input = sys.stdin.readline

N, M = map(int, input().split())
graph = [list(map(int, input().strip())) for _ in range(N)]
visit = [[[0] * 2 for _ in range(M)] for _ in range(N)]

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

def bfs() :
    queue = deque()
    queue.append((0, 0, 0))
    visit[0][0][0] = 1
    
    while queue :
        x, y, broke = queue.popleft()
        if x == N - 1 and y == M - 1 :
            return visit[x][y][broke]
        for i in range(4) :
            nx, ny = x + dx[i], y + dy[i]
            if 0 <= nx < N and 0 <= ny < M :
                if graph[nx][ny] == 0 and visit[nx][ny][broke] == 0 :
                    visit[nx][ny][broke] = visit[x][y][broke] + 1
                    queue.append((nx, ny, broke))
                elif graph[nx][ny] == 1 and broke == 0 and visit[nx][ny][1] == 0 :
                    visit[nx][ny][1] = visit[x][y][broke] + 1
                    queue.append((nx, ny, 1))
    return -1
print(bfs())