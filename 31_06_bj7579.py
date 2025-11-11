#   작성자 : 컴퓨터공학부 최완우
#   작성일 : 2025.11.11

import sys
input = sys.stdin.readline

n, m = map(int, input().split())
memories = list(map(int, input().split()))
costs = list(map(int, input().split()))

total_cost = sum(costs)
dp = [0] * (total_cost + 1)

for i in range(n) :
    for j in range(total_cost, costs[i] - 1, -1) :
        dp[j] = max(dp[j], dp[j - costs[i]] + memories[i])
        
for cost in range(total_cost + 1) :
    if dp[cost] >= m :
        print(cost)
        break