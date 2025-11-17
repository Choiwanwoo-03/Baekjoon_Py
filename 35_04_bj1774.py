#   작성자 : 컴퓨터공학부 최완우
#   작성일 : 2025.11.17

import sys
input = sys.stdin.readline

N, M = map(int, input().split())
star = [tuple(map(int, input().split())) for _ in range(N)]

parent = list(range(N + 1))

def solve(x) :
    if parent[x] != x :
        parent[x] = solve(parent[x])
    return parent[x]

def union(a, b) :
    pa = solve(a)
    pb = solve(b)
    if pa == pb :
        return False
    if pa < pb :
        parent[pb] = pa
    else :
        parent[pa] = pb
    return True

for _ in range(M) :
    a, b = map(int, input().split())
    union(a, b)

edge = []
for i in range(N) :
    for j in range(i + 1, N) :
        x1, y1 = star[i]
        x2, y2 = star[j]
        dist = ((x1 - x2) ** 2 + (y1 - y2) ** 2) ** 0.5
        edge.append((dist, i + 1, j + 1))
        
edge.sort()
total = 0.0
used_edge = 0

for dist, a, b in edge :
    if union(a, b) :
        total += dist
        used_edge += 1
        if used_edge == N :
            break
        
print(f"{total:.2f}")