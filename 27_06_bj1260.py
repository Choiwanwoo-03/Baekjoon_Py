#   작성자 : 컴퓨터공학부 최완우
#   작성일 : 2025.11.05

import sys
from collections import deque
input = sys.stdin.readline

N, M, V = map(int, input().split())
graph = [[] for _ in range(N + 1)]
for _ in range(M) :
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)
    
for i in range(1, N + 1) :
    graph[i].sort()
    
def dfs(v, visit) :
    visit[v] = True
    print(v, end = ' ')
    for i in graph[v] :
        if not visit[i] :
            dfs(i, visit)

def bfs(v, visit) :
    queue = deque([v])
    visit[v] = True
    while queue :
        node = queue.popleft()
        print(node, end = ' ')
        for i in graph[node] :
            if not visit[i] :
                queue.append(i)
                visit[i] = True

visit = [False] * (N + 1)
dfs(V, visit)
print()
visit = [False] * (N + 1)
bfs(V, visit)