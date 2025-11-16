#   작성자 : 컴퓨터공학부 최완우
#   작성일 : 2025.11.16

import sys
sys.setrecursionlimit(10 ** 9)
input = sys.stdin.readline

def find(x) :
    if parent[x] != x :
        parent[x] = find(parent[x])
    return parent[x]

def union(a, b) :
    ra = find(a)
    rb = find(b)
    if ra == rb :
        return
    
    if rank[ra] < rank[rb] :
        parent[ra] = rb
    else :
        parent[rb] = ra
        if rank[ra] == rank[rb] :
            rank[ra] += 1
            
n, m = map(int, input().split())
parent = [i for i in range(n + 1)]
rank = [0] * (n + 1)

for _ in range(m) :
    op, a, b = map(int, input().split())
    
    if op == 0 :
        union(a, b)
    else :
        print("YES" if find(a) == find(b) else "NO")