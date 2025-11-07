#   작성자 : 컴퓨터공학부 최완우
#   작성일 : 2025.11.07

from collections import deque
import sys
input = sys.stdin.readline

test = int(input())
for _ in range(test):
    n = int(input())
    data = list(map(int, input().split()))
    m = int(input())
    indegree = [0] * (n + 1)
    graph = [[False] * (n + 1) for _ in range(n + 1)]

    for i in range(n):
        for j in range(i + 1, n):
            graph[data[i]][data[j]] = True
            indegree[data[j]] += 1

    for _ in range(m):
        a, b = map(int, input().split())
        if graph[a][b]:
            graph[a][b] = False
            graph[b][a] = True
            indegree[a] += 1
            indegree[b] -= 1
        else:
            graph[b][a] = False
            graph[a][b] = True
            indegree[b] += 1
            indegree[a] -= 1

    queue = deque()
    answer = []
    for i in range(1, n + 1):
        if indegree[i] == 0:
            queue.append(i)
    certain = True
    cycle = False
    for _ in range(n):
        if len(queue) == 0:
            cycle = True
            break
        if len(queue) > 1:
            certain = False
            break
        now = queue.popleft()
        answer.append(now)
        for j in range(1, n + 1):
            if graph[now][j]:
                indegree[j] -= 1
                if indegree[j] == 0:
                    queue.append(j)
    if cycle:
        print("IMPOSSIBLE")
    elif not certain:
        print("?")
    else:
        print(' '.join(map(str, answer)))
