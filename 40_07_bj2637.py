#   작성자 : 컴퓨터공학부 최완우
#   작성일 : 2025.11.28

import sys
from collections import deque

input = sys.stdin.read

def solve():
    data = input().split()
    
    N = int(data[0]) 
    M = int(data[1])
    
    relations = []
    idx = 2
    for _ in range(M):
        X = int(data[idx])
        Y = int(data[idx+1])
        K = int(data[idx+2])
        relations.append((X, Y, K))
        idx += 3

    adj = [[] for _ in range(N + 1)]
    in_degree = [0] * (N + 1)
    is_intermediate = [False] * (N + 1) 

    for X, Y, K in relations:
        adj[Y].append((X, K))
        in_degree[X] += 1
        is_intermediate[X] = True
    dp = [[0] * (N + 1) for _ in range(N + 1)] 
    
    queue = deque()

    for i in range(1, N + 1):
        if in_degree[i] == 0:
            queue.append(i)
            dp[i][i] = 1 

    while queue:
        current_part = queue.popleft() 

        for next_part, count in adj[current_part]:
            for j in range(1, N + 1):
                dp[next_part][j] += dp[current_part][j] * count
                
            in_degree[next_part] -= 1
            
            if in_degree[next_part] == 0:
                queue.append(next_part)
    result = []
    for i in range(1, N):
        if not is_intermediate[i]: 
            required_count = dp[N][i]
            if required_count > 0:
                result.append(f"{i} {required_count}")

    print('\n'.join(result))

if __name__ == "__main__":
    solve()