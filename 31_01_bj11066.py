#   작성자 : 컴퓨터공학부 최완우
#   작성일 : 2025.11.10

import sys

def solve():
    T = int(sys.stdin.readline())
    
    for _ in range(T):
        K = int(sys.stdin.readline())
        files = list(map(int, sys.stdin.readline().split()))
        
        S = [0] * (K + 1)
        for i in range(K):
            S[i+1] = S[i] + files[i]

        def get_sum(i, j):
            return S[j+1] - S[i]

        INF = float('inf')
        dp = [[0] * K for _ in range(K)]
        A = [[0] * K for _ in range(K)] 

        for i in range(K):
            dp[i][i] = 0
            A[i][i] = i

        for i in range(K - 1):
            j = i + 1
            dp[i][j] = files[i] + files[j]
            A[i][j] = i

        for length in range(3, K + 1):
            for i in range(K - length + 1):
                j = i + length - 1
                
                dp[i][j] = INF
                current_sum = get_sum(i, j)
                
                start_k = A[i][j-1]
                end_k = A[i+1][j]
                
                for k in range(start_k, end_k + 1):
                    cost = dp[i][k] + dp[k+1][j] + current_sum
                    
                    if cost < dp[i][j]:
                        dp[i][j] = cost
                        A[i][j] = k 

        print(dp[0][K-1])

if __name__ == "__main__":
    solve()