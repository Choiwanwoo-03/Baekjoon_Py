#   작성자 : 컴퓨터공학부 최완우
#   작성일 : 2025.11.05

import sys
input = sys.stdin.readline

N = int(input())
house = [list(map(int, input().rstrip())) for _ in range(N)]
visit = [[False] * N for _ in range(N)]
result = []
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

def dfs(x, y) :
    visit[x][y] = True
    cnt = 1
    for i in range(4) :
        nx = x + dx[i]
        ny = y + dy[i]
        if 0 <= nx < N and 0 <= ny < N :
            if house[nx][ny] == 1 and not visit[nx][ny]:
                cnt += dfs(nx, ny)
    return cnt

for i in range(N) :
    for j in range(N) :
        if house[i][j] == 1 and not visit[i][j] :
            result.append(dfs(i, j))
print(len(result))
for num in sorted(result) :
    print(num)
