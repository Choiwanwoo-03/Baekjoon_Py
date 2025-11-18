#   작성자 : 컴퓨터공학부 최완우
#   작성일 : 2025.11.18

import sys
sys.setrecursionlimit(10 ** 6)
input = sys.stdin.readline

N = int(input())
graph = [[] for _ in range(N + 1)]

for _ in range(N - 1) :
    u, v = map(int, input().split())
    graph[u].append(v)
    graph[v].append(u)
    
dp = [[0, 0] for _ in range(N + 1)]

def dfs(node, parent) :
    dp[node][0] = 0
    dp[node][1] = 1
    
    for child in graph[node] :
        if child != parent :
            dfs(child, node)
            dp[node][0] += dp[child][1]
            dp[node][1] += min(dp[child][0], dp[child][1])
            
dfs(1, -1)
print(min(dp[1][0], dp[1][1]))