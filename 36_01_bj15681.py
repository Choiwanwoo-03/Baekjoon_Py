#   작성자 : 컴퓨터공학부 최완우
#   작성일 : 2025.11.18

import sys
sys.setrecursionlimit(10 ** 9)
input = sys.stdin.readline

N, R, Q = map(int, input().split())
graph = [[] for _ in range(N + 1)]

for _ in range(N - 1) :
    u, v = map(int, input().split())
    graph[u].append(v)
    graph[v].append(u)
    
subtree = [0] * (N + 1)

def dfs(node, parent) :
    subtree[node] = 1
    for child in graph[node] :
        if child != parent :
            dfs(child, node)
            subtree[node] += subtree[child]

dfs(R, -1)

for _ in range(Q) :
    u = int(input())
    print(subtree[u])