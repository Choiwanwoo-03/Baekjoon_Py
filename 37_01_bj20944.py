#   작성자 : 컴퓨터공학부 최완우
#   작성일 : 2025.11.19

import sys
sys.setrecursionlimit(300010)

input = sys.stdin.read
data = input().split()

index = 0
N = int(data[index])
index += 1

adj = [[] for _ in range(N + 1)]
for _ in range(N - 1):
    u = int(data[index])
    v = int(data[index + 1])
    w = int(data[index + 2])
    adj[u].append((v, w))
    adj[v].append((u, w))
    index += 3

size = [1] * (N + 1)
total = [0]
answer = [0] * (N + 1)

def solve(u, parent, depth):
    total[0] += depth
    for v, w in adj[u]:
        if v != parent:
            solve(v, u, depth + w)
            size[u] += size[v]

def dfs(u, parent):
    for v, w in adj[u]:
        if v != parent:
            answer[v] = answer[u] + (N - 2 * size[v]) * w
            dfs(v, u)

solve(1, 0, 0)
answer[1] = total[0]
dfs(1, 0)

for i in range(1, N + 1):
    print(answer[i])