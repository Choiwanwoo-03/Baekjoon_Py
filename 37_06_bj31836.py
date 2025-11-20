#   작성자 : 컴퓨터공학부 최완우
#   작성일 : 2025.11.20

import sys
input = sys.stdin.readline

N = int(input().strip())

A = []
B = []

if N == 2 :
    A = [1]
    B = [2]
else:
    r = (N - 2) % 3
    if r == 0:
        A = [1]
        B = [2]
        start = 5
    elif r == 1 :
        A = [1, 2]
        B = [3]
        start = 6
    else :
        A = [1, 3]
        B = [4]
        start = 7

    for i in range(start, N + 1, 3) :
        A.append(i - 2)
        A.append(i - 1)
        B.append(i)

print(len(A))
if A :
    print(*A)
else :
    print()
print(len(B))
if B :
    print(*B)
else :
    print()