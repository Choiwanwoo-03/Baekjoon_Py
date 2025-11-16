#   작성자 : 컴퓨터공학부 최완우
#   작성일 : 2025.11.16

import sys
input = sys.stdin.readline

def find(x) :
    if parent[x] != x :
        parent[x] = find(parent[x])
    return parent[x]

def union(a, b) :
    ra = find(a)
    rb = find(b)
    if ra == rb :
        return size[ra]
    if size[ra] < size[rb] :
        ra, rb = rb, ra
    parent[rb] = ra
    size[ra] += size[rb]
    return size[ra]

t = int(input().strip())
for _ in range(t) :
    F = int(input().strip())
    max_node = 2 * F + 5
    parent = [i for i in range(max_node)]
    size = [1] * max_node
    
    id_name = {}
    next_id = 1
    
    for _ in range(F) :
        a_name, b_name = input().split()
        if a_name not in id_name :
            id_name[a_name] = next_id
            next_id += 1
        if b_name not in id_name :
            id_name[b_name] = next_id
            next_id += 1
            
        a = id_name[a_name]
        b = id_name[b_name]
        
        ans = union(a, b)
        print(ans)