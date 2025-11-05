#   작성자 : 컴퓨터공학부 최완우
#   작성일 : 2025.11.05

import sys
sys.setrecursionlimit(10 ** 6)

input = sys.stdin.readline

n = int(input())
m = int(input())

graph = [[] for _ in range(n + 1)]
visit = [False] * (n + 1)
count = 0

for _ in range(m) :
    u, v = map(int, input().split())
    graph[u].append(v)
    graph[v].append(u)
    
def dfs(node) :
    global count
    visit[node] = True
    for next_node in graph[node] :
        if not visit[next_node] :
            count += 1
            dfs(next_node)

dfs(1)
print(count)