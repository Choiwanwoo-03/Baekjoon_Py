#   작성자 : 컴퓨터공학부 최완우
#   작성일 : 2025.11.28

import sys

def main():
    data = list(map(int, sys.stdin.read().split()))
    if not data:
        return

    N, T, M, S, E = data[:5]
    edges = data[5:]

    INF = 10**18
    dp = [[INF] * N for _ in range(T + 1)]
    dp[0][S] = 0

    idx = 0

    for t in range(T):
        for v in range(N):
            dp[t + 1][v] = dp[t][v]

        for _ in range(M):
            x = edges[idx]
            y = edges[idx + 1]
            w = edges[idx + 2]
            idx += 3

            if dp[t][x] + w < dp[t + 1][y]:
                dp[t + 1][y] = dp[t][x] + w
            if dp[t][y] + w < dp[t + 1][x]:
                dp[t + 1][x] = dp[t][y] + w

    ans = dp[T][E]
    print(ans if ans < INF else -1)

if __name__ == "__main__":
    main()