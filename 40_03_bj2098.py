#   작성자 : 컴퓨터공학부 최완우
#   작성일 : 2025.11.27

import sys
sys.setrecursionlimit(2000)
input = sys.stdin.read

def solve():
    data = input().split()
    if not data:
        return

    N = int(data[0])
    
    W = [[0] * N for _ in range(N)]
    
    data_idx = 1
    for i in range(N):
        for j in range(N):
            W[i][j] = int(data[data_idx])
            data_idx += 1

    DP = [[-1] * (1 << N) for _ in range(N)] 

    INF = float('inf')

    def find_path(current, visited_mask):
        if visited_mask == (1 << N) - 1:
            if W[current][0] != 0:
                return W[current][0]
            else:
                return INF

        if DP[current][visited_mask] != -1:
            return DP[current][visited_mask]

        min_cost = INF
        
        for next_city in range(N):
            if W[current][next_city] != 0 and not (visited_mask & (1 << next_city)):
                
                new_mask = visited_mask | (1 << next_city)
                
                cost = W[current][next_city] + find_path(next_city, new_mask)
                
                min_cost = min(min_cost, cost)

        DP[current][visited_mask] = min_cost
        
        return min_cost

    result = find_path(0, 1)

    print(result)

solve()