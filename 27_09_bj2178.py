#   작성자 : 컴퓨터공학부 최완우
#   작성일 : 2025.11.05

import sys
from collections import deque
input = sys.stdin.readline

N, M = map(int, input().split())
maze = [list(map(int, input().rstrip())) for _ in range(N)]
visit = [[False] * M for _ in range(N)]
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

def bfs(X, Y) :
    queue = deque()
    queue.append((X, Y))
    visit[X][Y] = True
    while queue :
        a, b = queue.popleft()
        for i in range(4) :
            nx, ny = a + dx[i], b + dy[i]
            if 0 <= nx < N and 0 <= ny < M :
                if maze[nx][ny] == 1 and not visit[nx][ny] :
                    maze[nx][ny] = maze[a][b] + 1
                    visit[nx][ny] = True
                    queue.append((nx, ny))
    return maze[N - 1][M - 1]

print(bfs(0, 0))