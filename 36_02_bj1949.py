#   작성자 : 컴퓨터공학부 최완우
#   작성일 : 2025.11.18

import sys
sys.setrecursionlimit(10 ** 6)
input = sys.stdin.readline

N = int(input())
people = [0] + list(map(int, input().split()))
graph = [[] for _ in range(N + 1)]

for _ in range(N - 1) :
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)
    
dp = [[0, 0] for _ in range(N + 1)]

def dfs(node, parent) :
    dp[node][0] = 0
    dp[node][1] = people[node]
    
    for child in graph[node] :
        if child != parent :
            dfs(child, node)
            dp[node][0] += max(dp[child][0], dp[child][1])
            dp[node][1] += dp[child][0]
            
dfs(1, -1)
print(max(dp[1][0], dp[1][1]))