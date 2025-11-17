#   작성자 : 컴퓨터공학부 최완우
#   작성일 : 2025.11.17

import sys
input = sys.stdin.readline

n = int(input())
star = []
for _ in range(n) :
    x, y = map(float, input().split())
    star.append((x, y))

edge = []
for i in range(n) :
    for j in range(i+1, n) :
        x1, y1 = star[i]
        x2, y2 = star[j]
        dist = ((x1-x2) ** 2 + (y1-y2) ** 2) ** 0.5
        edge.append((dist, i, j))

edge.sort()

parent = [i for i in range(n)]

def solve(x) :
    if parent[x] != x :
        parent[x] = solve(parent[x])
    return parent[x]

def union(a, b) :
    a = solve(a)
    b = solve(b)
    if a < b :
        parent[b] = a
    else:
        parent[a] = b

total = 0
for dist, a, b in edge :
    if solve(a) != solve(b) :
        union(a, b)
        total += dist

print(total)