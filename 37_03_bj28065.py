#   작성자 : 컴퓨터공학부 최완우
#   작성일 : 2025.11.19

import sys
input = sys.stdin.readline

n = int(input().strip())
L, R = 1, n
ans = []

while L < R :
    ans.append(L)
    ans.append(R)
    L += 1
    R -= 1

if L == R :
    ans.append(L)

print(*ans)