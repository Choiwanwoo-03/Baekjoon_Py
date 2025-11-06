#   작성자 : 컴퓨터공학부 최완우
#   작성일 : 2025.11.06

import sys
from collections import deque
input = sys.stdin.readline

M, N = map(int, input().split())
box = [list(map(int, input().split())) for _ in range(N)]
queue = deque()

for i in range(N) :
    for j in range(M) :
        if box[i][j] == 1 :
            queue.append((i, j))
            
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]
while queue :
    x, y = queue.popleft()
    for d in range(4) :
        nx, ny = x+ dx[d], y + dy[d]
        if 0 <= nx < N and 0 <= ny < M and box[nx][ny] == 0 :
            box[nx][ny] = box[x][y] + 1
            queue.append((nx, ny))
            
result = 0
for row in box :
    for value in row :
        if value == 0 :
            print(-1)
            sys.exit(0)
        result = max(result, value)
print(result - 1)