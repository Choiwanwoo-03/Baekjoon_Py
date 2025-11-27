#   작성자 : 컴퓨터공학부 최완우
#   작성일 : 2025.11.27

import sys

INF = 1000 * 1000 + 1

def solve() :
    input = sys.stdin.read
    data = input().split()
    
    if not data :
        return
    N = int(data[0])
    
    cost = []
    data_idx = 1
    for i in range(N) :
        cost.append([int(data[data_idx]), int(data[data_idx + 1]), int(data[data_idx + 2])])
        data_idx += 3
        
    if N == 1 :
        print(min(cost[0]))
        return
    
    min_total_cost = INF
    
    for start_color in range(3) :
        DP = [[0] * 3 for _ in range(N)]
        
        for color in range(3) :
            if color == start_color :
                DP[0][color] = cost[0][color]
            else :
                DP[0][color] = INF
                
        for i in range(1, N) :
            DP[i][0] = cost[i][0] + min(DP[i - 1][1], DP[i - 1][2])
            DP[i][1] = cost[i][1] + min(DP[i - 1][0], DP[i - 1][2])
            DP[i][2] = cost[i][2] + min(DP[i - 1][0], DP[i - 1][1])
        
        for end_color in range(3) :
            if end_color != start_color :
                min_total_cost = min(min_total_cost, DP[N - 1][end_color])
            
    print(min_total_cost)
solve()