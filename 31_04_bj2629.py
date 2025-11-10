#   작성자 : 컴퓨터공학부 최완우
#   작성일 : 2025.11.10

import sys
sys.setrecursionlimit(10**6) 

def solve():
    N = int(sys.stdin.readline())
    weights = list(map(int, sys.stdin.readline().split()))
    
    M = int(sys.stdin.readline())
    beads = list(map(int, sys.stdin.readline().split()))
    MAX_WEIGHT = sum(weights) 
    dp = [[False] * (MAX_WEIGHT + 1) for _ in range(N + 1)]

    def dfs(index, current_weight):
        if index > N:
            return
        
        if 0 <= current_weight <= MAX_WEIGHT and dp[index][current_weight]:
            return
        
        if 0 <= current_weight <= MAX_WEIGHT:
            dp[index][current_weight] = True
                    
        next_weight = weights[index - 1]        
        dfs(index + 1, current_weight) 
        dfs(index + 1, abs(current_weight - next_weight))
        dfs(index + 1, current_weight + next_weight)
    dfs(0, 0)

    result = []
    for bead_weight in beads:
        if bead_weight > MAX_WEIGHT or bead_weight > 40000:
            result.append('N')
            continue
        if dp[N][bead_weight]:
            result.append('Y')
        else:
            result.append('N')
            
    print(' '.join(result))

if __name__ == "__main__":
    solve()