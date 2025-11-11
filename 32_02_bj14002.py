#   작성자 : 컴퓨터공학부 최완우
#   작성일 : 2025.11.11

import sys
input = sys.stdin.readline

N = int(input())
A = list(map(int, input().split()))

dp = [1] * N
index = [-1] * N

for i in range(N) :
    for j in range(i) :
        if A[i] > A[j] and dp[i] < dp[j] + 1 :
            dp[i] = dp[j] + 1
            index[i] = j
            
length = max(dp)
idx = dp.index(length)

arr = []
while idx != -1 :
    arr.append(A[idx])
    idx = index[idx]
arr.reverse()

print(length)
print(*arr)