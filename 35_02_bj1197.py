#   작성자 : 컴퓨터공학부 최완우
#   작성일 : 2025.11.17

import sys
input = sys.stdin.readline

V, E = map(int, input().split())
edge = [tuple(map(int, input().split())) for _ in range(E)]
edge.sort(key=lambda x: x[2])

parent = list(range(V + 1))

def find(x) :
    root = x
    while parent[root] != root:
        root = parent[root]
    while x != root :
        parent[x], x = root, parent[x]
    return root

def union(a, b) :
    pa, pb = find(a), find(b)
    if pa == pb : 
        return False
    if pa < pb :
        parent[pb] = pa
    else :
        parent[pa] = pb
    return True

total = 0
for a, b, cost in edge :
    if union(a, b) :
        total += cost
        if total > 10 ** 9 :
            break

print(total)