#   작성자 : 컴퓨터공학부 최완우
#   작성일 : 2025.11.13

import sys
sys.setrecursionlimit(10 ** 6)
input = sys.stdin.readline

V = int(input())
graph = [[] for _ in range(V + 1)]

for _ in range(V) :
    data = list(map(int, input().split()))
    node = data[0]
    for i in range(1, len(data) - 1, 2) :
        next_node, dist = data[i], data[i + 1]
        graph[node].append((next_node, dist))

def dfs(node, dist) :
    for next_node, next_dist in graph[node] :
        if distance[next_node] == -1 :
            distance[next_node] = dist + next_dist
            dfs(next_node, dist + next_dist)

distance = [-1] * (V + 1)
distance[1] = 0
dfs(1, 0)

farthest_node = distance.index(max(distance))

distance = [-1] * (V + 1)
distance[farthest_node] = 0
dfs(farthest_node, 0)

print(max(distance))