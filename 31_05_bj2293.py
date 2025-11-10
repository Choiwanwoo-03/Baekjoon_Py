#   작성자 : 컴퓨터공학부 최완우
#   작성일 : 2025.11.10

import sys
input = sys.stdin.read 

def solve():
    data = input().split()
    
    if not data:
        return

    N = int(data[0])
    K = int(data[1])
    
    coins = [int(data[i]) for i in range(2, 2 + N)]
    dp = [0] * (K + 1)
    dp[0] = 1 

    for coin in coins:
        for amount in range(coin, K + 1):
            dp[amount] += dp[amount - coin]
            
    print(dp[K])

if __name__ == "__main__":
    solve()