#   작성자 : 컴퓨터공학부 최완우
#   작성일 : 2025.11.10

import sys
sys.setrecursionlimit(10**7) 

def solve():
    M, N = map(int, sys.stdin.readline().split()) # M: 세로 (행), N: 가로 (열)
    Map = []
    for _ in range(M):
        Map.append(list(map(int, sys.stdin.readline().split())))

    dp = [[-1] * N for _ in range(M)]

    dx = [0, 0, 1, -1]
    dy = [1, -1, 0, 0]

    def dfs(x, y):        
        if x == M - 1 and y == N - 1:
            return 1

        if dp[x][y] != -1:
            return dp[x][y]

        dp[x][y] = 0
        
        for i in range(4):
            nx, ny = x + dx[i], y + dy[i]

            if 0 <= nx < M and 0 <= ny < N:
                if Map[x][y] > Map[nx][ny]:
                    dp[x][y] += dfs(nx, ny)
        
        return dp[x][y]

    result = dfs(0, 0)
    print(result)

if __name__ == "__main__":
    solve()