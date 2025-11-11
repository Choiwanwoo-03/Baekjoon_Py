#   작성자 : 컴퓨터공학부 최완우
#   작성일 : 2025.11.11

import sys
input = sys.stdin.readline
import bisect

N = int(input())
A = list(map(int, input().split()))
arr = []
temp = [0] * N
for i, x in enumerate(A) :
    idx = bisect.bisect_left(arr, x)
    if idx == len(arr) :
        arr.append(x)
    else :
        arr[idx] = x
    temp[i] = idx
length = len(arr)
print(length)

ans = []
now = length - 1
for i in range(N - 1, -1, -1) :
    if temp[i] == now :
        ans.append(A[i])
        now -= 1
ans.reverse()
print(*ans)