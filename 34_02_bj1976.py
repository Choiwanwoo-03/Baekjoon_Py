#   작성자 : 컴퓨터공학부 최완우
#   작성일 : 2025.11.16

import sys
input = sys.stdin.readline

N = int(input())
M = int(input())

parent = [i for i in range(N + 1)]

def find(x) :
    if parent[x] != x :
        parent[x] = find(parent[x])
    return parent[x]

def solve(A, B) :
    A = find(A)
    B = find(B)
    if A != B :
        parent[B] = A
        
for i in range(1, N + 1) :
    row = list(map(int, input().split()))
    for j in range(1, N + 1) :
        if row[j - 1] == 1 :
            solve(i, j)

plan = list(map(int, input().split()))

root = find(plan[0])
answer = True

for p in plan[1:] :
    if find(p) != root :
        answer = False
        break
    
print("YES" if answer else "NO")