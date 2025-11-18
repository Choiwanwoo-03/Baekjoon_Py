#   작성자 : 컴퓨터공학부 최완우
#   작성일 : 2025.11.18

from collections import deque
import sys
input = sys.stdin.readline

N, M = map(int, input().split())
graph = [list(map(int, input().split())) for _ in range(N)]

dx = [0, 0, 1, -1]
dy = [1, -1, 0, 0]

visit = [[False] * M for _ in range(N)]
count = 0
island = [[0] * M for _ in range(N)]

def solve(x, y, num):
    q = deque([(x, y)])
    visit[x][y] = True
    island[x][y] = num
    
    while q:
        x, y = q.popleft()
        for i in range(4):
            nx, ny = x + dx[i], y + dy[i]
            if 0 <= nx < N and 0 <= ny < M and not visit[nx][ny] and graph[nx][ny] == 1:
                visit[nx][ny] = True
                island[nx][ny] = num
                q.append((nx, ny))

for i in range(N):
    for j in range(M):
        if graph[i][j] == 1 and not visit[i][j]:
            count += 1
            solve(i, j, count)

edge = []

def find(x, y, id, idx):
    d = 0
    nx, ny = x + dx[idx], y + dy[idx]
    
    while 0 <= nx < N and 0 <= ny < M:
        if graph[nx][ny] == 1:
            if island[nx][ny] != id and d >= 2:
                edge.append((d, id, island[nx][ny]))
            break
        if graph[nx][ny] == 0:
            d += 1
        nx += dx[idx]
        ny += dy[idx]

for i in range(N):
    for j in range(M):
        if graph[i][j] == 1:
            for d in range(4):
                find(i, j, island[i][j], d)

parent = [i for i in range(count + 1)]

def find_p(x):
    if parent[x] != x:
        parent[x] = find_p(parent[x])
    return parent[x]

def union(a, b):
    a = find_p(a)
    b = find_p(b)
    if a < b:
        parent[b] = a
    else:
        parent[a] = b

edge.sort()
total = 0
used_edge = 0

for cost, a, b in edge:
    if find_p(a) != find_p(b):
        union(a, b)
        total += cost
        used_edge += 1

if used_edge == count - 1:
    print(total)
else:
    print(-1)