#   작성자 : 컴퓨터공학부 최완우
#   작성일 : 2025.11.06

import sys
from collections import deque
input = sys.stdin.readline

M, N, H = map(int, input().split())
box = [[list(map(int, input().split())) for _ in range(N)] for _ in range(H)]
queue = deque()

for z in range(H) :
    for x in range(N) :
        for y in range(M) :
            if box[z][x][y] == 1:
                queue.append((z, x, y))
                
dz = [0, 0, 0, 0, 1, -1]
dx = [-1, 1, 0, 0, 0, 0]
dy = [0, 0, -1, 1, 0, 0]

while queue :
    z, x, y = queue.popleft()
    for i in range(6) :
        nz, nx, ny = z + dz[i], x + dx[i], y + dy[i]
        if 0 <= nz < H and 0 <= nx < N and 0 <= ny < M and box[nz][nx][ny] == 0 :
            box[nz][nx][ny] = box[z][x][y] + 1
            queue.append((nz, nx, ny))
            
ans = 0
for z in range(H) :
    for x in range(N) :
        for y in range(M) :
            if box[z][x][y] == 0 :
                print(-1)
                sys.exit(0)
            ans = max(ans, box[z][x][y])
print(ans - 1)