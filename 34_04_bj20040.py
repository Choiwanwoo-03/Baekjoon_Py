#   작성자 : 컴퓨터공학부 최완우
#   작성일 : 2025.11.16

import sys
sys.setrecursionlimit(10 ** 9)
input = sys.stdin.readline

def find(x) :
    if parent[x] != x :
        parent[x] = find(parent[x])
    return parent[x]

def solve(a, b) :
    a = find(a)
    b = find(b)
    if a != b :
        if size[a] < size[b] :
            a, b = b, a
        parent[b] = a
        size[a] += size[b]
        
n, m = map(int, input().split())
parent = [i for i in range(n)]
size = [1] * n

ansewr = 0

for i in range(1, m + 1) :
    a, b = map(int, input().split())
    
    if find(a) == find(b) :
        answer = i
        break
    else :
        solve(a, b)
        
print(answer)