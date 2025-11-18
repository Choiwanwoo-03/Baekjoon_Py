#   작성자 : 컴퓨터공학부 최완우
#   작성일 : 2025.11.18

import sys
sys.setrecursionlimit(10 ** 6)
input = sys.stdin.readline

N = int(input())
weight = [0] + list(map(int, input().split()))
graph = [[] for _ in range(N + 1)]

for _ in range(N - 1) :
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)
    
dp = [[0, 0] for _ in range(N + 1)]
select = [[] for _ in range(N + 1)]

def dfs(node, parent) :
    dp[node][0] = 0
    dp[node][1] = weight[node]
    select[node] = [[], [node]]
    
    for child in graph[node] :
        if child != parent :
            dfs(child, node)
            
            if dp[node][0] < dp[node][0] + max(dp[child][0], dp[child][1]) :
                dp[node][0] = dp[node][0] + max(dp[child][0], dp[child][1])
                
                if dp[child][0] > dp[child][1] :
                    select[node][0] = select[child][0]
                else :
                    select[node][0] = select[node][0][:]
                select[node][0] = select[node][0][:]
                
            new_val = dp[node][1] + dp[child][0]
            if new_val > dp[node][1] :
                dp[node][1] = new_val
                select[node][1] = [node] + select[child][0]