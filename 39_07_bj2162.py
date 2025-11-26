#   작성자 : 컴퓨터공학부 최완우
#   작성일 : 2025.11.26

import sys
input = sys.stdin.readline

def find(x) :
    if parent[x] != x :
        parent[x] = find(parent[x])
    return parent[x]

def union(a, b) :
    a = find(a)
    b = find(b)
    if a < b :
        parent[b] = a
    else :
        parent[a] = b
        
def ccw(x1, y1, x2, y2, x3, y3) :
    val = (x2 - x1) * (y3 - y1) - (x3 - x1) * (y2 - y1)
    if val > 0 :
        return 1
    elif val < 0 :
         return -1
    else :
        return 0
    
def solve(l1, l2) :
    x1, y1, x2, y2 = l1
    x3, y3, x4, y4 = l2
    
    res1 = ccw(x1, y1, x2, y2, x3, y3) * ccw(x1, y1, x2, y2, x4, y4)
    res2 = ccw(x3, y3, x4, y4, x1, y1) * ccw(x3, y3, x4, y4, x2, y2)
    
    if res1 == 0 and res2 == 0 :
        if (x1, y1) > (x2, y2) : x1, y1, x2, y2 = x2, y2, x1, y1
        if (x3, y3) > (x4, y4) : x3, y3, x4, y4 = x4, y4, x3, y3
        return (x1, y1) <= (x4, y4) and (x3, y3) <= (x2, y2)
    return res1 <= 0 and res2 <= 0

N = int(input())
lines = []
parent = [i for i in range(N)]

for _ in range(N) :
    lines.append(list(map(int, input().split())))
    
for i in range(N) :
    for j in range(i + 1, N) :
        if solve(lines[i], lines[j]) :
            union(i, j)
            
count = {}
for i in range(N) :
    root = find(i)
    if root not in count :
        count[root] = 0
    count[root] += 1
    
print(len(count))
print(max(count.values()))