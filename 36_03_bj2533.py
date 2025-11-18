#   작성자 : 컴퓨터공학부 최완우
#   작성일 : 2025.11.18

import sys
sys.setrecursionlimit(10 ** 7)
input = sys.stdin.readline

N = int(input())
weights = [0] + list(map(int, input().split()))

graph = [[] for _ in range(N + 1)]

for _ in range(N - 1) :
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)

dp = [[0, 0] for _ in range(N + 1)]
visited = [False] * (N + 1)

def dfs(u) :
    visited[u] = True
    dp[u][0] = 0
    dp[u][1] = weights[u]

    for v in graph[u] :
        if not visited[v] :
            dfs(v)
            dp[u][0] += max(dp[v][0], dp[v][1])
            dp[u][1] += dp[v][0]

selected = []

def trace(u, choose, parent) :
    if choose == 1 :
        selected.append(u)
        for v in graph[u] :
            if v != parent :
                trace(v, 0, u)
    else:
        for v in graph[u] :
            if v != parent :
                if dp[v][1] > dp[v][0] :
                    trace(v, 1, u)
                else :
                    trace(v, 0, u)


dfs(1)

if dp[1][1] > dp[1][0] :
    trace(1, 1, -1)
else :
    trace(1, 0, -1)

selected.sort()

print(max(dp[1][0], dp[1][1]))
print(*selected)