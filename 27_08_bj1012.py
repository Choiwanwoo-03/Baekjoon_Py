#   작성자 : 컴퓨터공학부 최완우
#   작성일 : 2025.11.05

import sys
sys.setrecursionlimit(10000)
input = sys.stdin.readline

T = int(input())
for _ in range(T) :
    M, N, K = map(int, input().split())
    field = [[0] * M for _ in range(N)]
    visit = [[False] * M for _ in range(N)]
    for _ in range(K) :
        X, Y = map(int, input().split())
        field[Y][X] = 1
        
    dx = [-1, 1, 0, 0]
    dy = [0, 0, -1, 1]
    
    def dfs(X, Y) :
        visit[Y][X] = True
        for i in range(4) :
            nx = X + dx[i]
            ny = Y + dy[i]
            if 0 <= nx < M and 0 <= ny < N :
                if field[ny][nx] == 1 and not visit[ny][nx] :
                    dfs(nx, ny)
                    
    count = 0
    for i in range(N) :
        for j in range(M) :
            if field[i][j] == 1 and not visit[i][j] :
                dfs(j, i)
                count += 1
    print(count)