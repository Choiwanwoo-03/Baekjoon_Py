#   작성자 : 컴퓨터공학부 최완우
#   작성일 : 2025.11.27

import sys

def solve_correct():
    try:
        N = int(sys.stdin.readline())
        K = int(sys.stdin.readline())
    except:
        return
    
    MOD = 1000000003
    if K * 2 > N:
        print(0)
        return
    
    DP = [[0] * (K + 1) for _ in range(N + 1)] 
    
    for i in range(N + 1):
        DP[i][0] = 1 
        
    for i in range(1, N + 1):
        DP[i][1] = i

    for i in range(2, N + 1):
        for j in range(2, K + 1):
            DP[i][j] = (DP[i-1][j] + DP[i-2][j-1]) % MOD

    case1 = DP[N-1][K]
    
    case2 = DP[N-3][K-1]
    
    result = (case1 + case2) % MOD

    print(result)

solve_correct()