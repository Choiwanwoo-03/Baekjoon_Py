#   작성자 : 컴퓨터공학부 최완우
#   작성일 : 2025.11.20

import sys
input = sys.stdin.readline

n, k = map(int, input().split())

if k > n - 1:
    print("Impossible")
    sys.exit(0)

p = (n - 1) - k

A = list(range(1, n + 1))

if p % 2 == 1:
    A[0], A[n - 1] = A[n - 1], A[0]
    p -= 1

i = 1
while p > 0 and i + 1 < n:
    A[i], A[i + 1] = A[i + 1], A[i]
    p -= 2
    i += 2

print(*A)
