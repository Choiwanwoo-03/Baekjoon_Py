#   작성자 : 컴퓨터공학부 최완우
#   작성일 : 2025.11.24

import sys
from collections import deque
input = sys.stdin.readline

N, D = map(int, input().split())
A = [0] + list(map(int, input().split()))

dp = [0] * (N + 1)
q = deque([0])
final_max_score = -float('inf')

for i in range(1, N + 1) :
    while q and q[0] < i - D :
        q.popleft()
    max_prev_dp = dp[q[0]]
    dp[i] = A[i] + max(max_prev_dp, 0)
    
    while q and dp[q[-1]] <= dp[i] :
        q.pop()
    q.append(i)
    final_max_score = max(final_max_score, dp[i])
print(final_max_score)