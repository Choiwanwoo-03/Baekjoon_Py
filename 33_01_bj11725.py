#   작성자 : 컴퓨터공학부 최완우
#   작성일 : 2025.11.13

import sys
sys.setrecursionlimit(10 ** 6)
input = sys.stdin.readline

N = int(input())
graph = [[] for _ in range(N + 1)]
for _ in range(N - 1) :
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)

parent = [0] * (N + 1)

def dfs(node, p) :
    for next_node in graph[node] :
        if next_node != p :
            parent[next_node] = node
            dfs(next_node, node)

dfs(1, 0)

for i in range(2, N + 1) :
    print(parent[i])