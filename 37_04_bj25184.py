#   작성자 : 컴퓨터공학부 최완우
#   작성일 : 2025.11.19

import sys
input = sys.stdin.readline

N = int(input())
half = N // 2

small = list(range(1, half + 1))
large = list(range(half + 1, N + 1))

ans = []
for s, l in zip(small, large) :
    ans.append(l)
    ans.append(s)

if N % 2 == 1 :
    ans.append(large[-1])

print(*ans)
