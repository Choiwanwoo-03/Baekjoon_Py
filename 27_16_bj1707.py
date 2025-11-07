#   작성자 : 컴퓨터공학부 최완우
#   작성일 : 2025.11.07

from collections import deque
import sys
input = sys.stdin.readline

K = int(input())
for _ in range(K) :
    V, E = map(int, input().split())
    graph = [[] for _ in range(V + 1)]
    visit = [0] * (V + 1)
    for _ in range(E) :
        u, v = map(int, input().split())
        graph[u].append(v)
        graph[v].append(u)
    result = True
    for i in range(1, V + 1) :
        if visit[i] == 0 :
            queue = deque()
            queue.append(i)
            visit[i] = 1
            while queue and result :
                node = queue.popleft()
                for neighbor in graph[node] :
                    if visit[neighbor] == 0 :
                        visit[neighbor] = -visit[node]
                        queue.append(neighbor)
                    elif visit[neighbor] == visit[node] :
                        result = False
                        break
    print("YES" if result else "NO")