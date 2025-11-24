#   작성자 : 컴퓨터공학부 최완우
#   작성일 : 2025.11.24

import sys
from collections import deque
input = sys.stdin.readline

n, k = map(int, input().split())
arr = [0] + [int(input()) for _ in range(n)]
arr.append(0)

dp = [0] * (n + 2)
q = deque([0])

for i in range(1, n + 2) :
    while q and q[0] < i - (k + 1) :
        q.popleft()
    
    dp[i] = dp[q[0]] + arr[i]
    while q and dp[q[-1]] > dp[i] :
        q.pop()
        
    q.append(i)
print(sum(arr) - dp[n + 1])