#   작성자 : 컴퓨터공학부 최완우
#   작성일 : 2025.11.17

import sys
input = sys.stdin.readline

while True :
    m, n = map(int, input().split())
    if m == 0 and n == 0 :
        break
    
    edge = []
    total = 0
    for _ in range(n) :
        x, y, z = map(int, input().split())
        edge.append((z, x, y))
        total += z
    
    edge.sort()
    
    parent = list(range(m))
    
    def solve(x) :
        if parent[x] != x :
            parent[x] = solve(parent[x])
        return parent[x]
    
    def union(a, b) :
        pa = solve(a)
        pb = solve(b)
        if pa < pb :
            parent[pb] = pa
        else :
            parent[pa] = pb
    
    use = 0
    for cost, a, b in edge:
        if solve(a) != solve(b):
            union(a, b)
            use += cost
    
    print(total - use)