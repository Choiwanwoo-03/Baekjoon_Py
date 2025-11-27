#   작성자 : 컴퓨터공학부 최완우
#   작성일 : 2025.11.27

import sys
import math

def solve_final():
    try:
        N = int(sys.stdin.readline().rstrip())
    except:
        return

    S = []
    for _ in range(N):
        S.append(sys.stdin.readline().rstrip())
        
    K = int(sys.stdin.readline().rstrip())
    
    S_rem = [int(s) % K for s in S]
    
    S_len = [len(s) for s in S]
    
    max_len = 0
    if N > 0:
        max_len = max(S_len)

    pow10_rem = [1] * (max_len + 1)
    for i in range(1, max_len + 1):
        pow10_rem[i] = (pow10_rem[i - 1] * 10) % K

    DP = [[0] * K for _ in range(1 << N)]
    for i in range(N):
        DP[1 << i][S_rem[i]] = 1

    for mask in range(1, 1 << N):
        for rem in range(K):
            if DP[mask][rem] > 0 :
                for next_i in range(N):
                    if not (mask & (1 << next_i)):
                        
                        len_next = S_len[next_i]
                        rem_next = S_rem[next_i]
                        
                        new_rem = (rem * pow10_rem[len_next] + rem_next) % K
                        
                        new_mask = mask | (1 << next_i)
                        
                        DP[new_mask][new_rem] += DP[mask][rem]
    final_mask = (1 << N) - 1
    p = DP[final_mask][0]
    q = math.factorial(N)

    if p == 0:
        print("0/1")
    else:
        g = math.gcd(p, q)
        print(f"{p // g}/{q // g}") 
        
solve_final()