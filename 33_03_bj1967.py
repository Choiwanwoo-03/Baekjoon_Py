#   작성자 : 컴퓨터공학부 최완우
#   작성일 : 2025.11.13

import sys
sys.setrecursionlimit(10 ** 6)
input = sys.stdin.readline

n = int(input())
graph = [[] for _ in range(n + 1)]

for _ in range(n - 1) :
    a, b, c = map(int, input().split())
    graph[a].append((b, c))
    graph[b].append((a, c))
    
def dfs(node, dist) :
    for next_node, cost in graph[node] :
        if distance[next_node] == -1 :
            distance[next_node] = dist + cost
            dfs(next_node, dist + cost)
            
distance = [-1] * (n + 1)
distance[1] = 0
dfs(1, 0)
fnode = distance.index(max(distance))

distance = [-1] * (n + 1)
distance[fnode] = 0
dfs(fnode, 0)

print(max(distance))