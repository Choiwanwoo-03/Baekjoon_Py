#   작성자 : 컴퓨터공학부 최완우
#   작성일 : 2025.11.12

import sys
sys.setrecursionlimit(10**6) 
input = sys.stdin.read

data = input().split()
N = int(data[0])
W = int(data[1])

cases = [[0, 0]] * (W + 2)
cases[0] = (1, 1)
cases[1] = (N, N)

for i in range(W):
    cases[i + 2] = (int(data[2 + 2 * i]), int(data[2 + 2 * i + 1]))

dp = [[-1] * (W + 2) for _ in range(W + 2)]
path = [[0] * (W + 2) for _ in range(W + 2)] 

def dist(p1, p2):
    return abs(cases[p1][0] - cases[p2][0]) + abs(cases[p1][1] - cases[p2][1])

def solve_dp(p1, p2):
    next_case = max(p1, p2) + 1     
    if next_case == W + 2:
        return 0
    if dp[p1][p2] != -1:
        return dp[p1][p2]
    cost1 = dist(p1, next_case) + solve_dp(next_case, p2)
    cost2 = dist(p2, next_case) + solve_dp(p1, next_case)
    if cost1 < cost2:
        dp[p1][p2] = cost1
        path[p1][p2] = 1
    else:
        dp[p1][p2] = cost2
        path[p1][p2] = 2
        
    return dp[p1][p2]

min_total_dist = solve_dp(0, 1)
print(min_total_dist)

p1, p2 = 0, 1
while max(p1, p2) < W + 1:
    car = path[p1][p2]
    print(car)
    
    next_case = max(p1, p2) + 1
    if car == 1:
        p1 = next_case
    else:
        p2 = next_case