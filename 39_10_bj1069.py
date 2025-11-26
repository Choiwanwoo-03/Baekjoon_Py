#   작성자 : 컴퓨터공학부 최완우
#   작성일 : 2025.11.26

import sys
import math
input = sys.stdin.readline

def solve() :
    X, Y, D, T = map(int, input().split())
    
    dist = math.sqrt(X ** 2 + Y ** 2)
    if D <= T :
        print("{:.10f}".format(dist))
        return
    n = dist // D
    
    if n == 0 :
        ans = min(dist, T + (D - dist), 2.0 * T)
        
    else :
        time1 = n * T + (dist - n * D)
        time2 = (n + 1) * T
        ans = min(time1, time2, dist)
        
    print("{:.10f}".format(ans))
solve()