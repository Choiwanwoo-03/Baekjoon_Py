#   작성자 : 컴퓨터공학부 최완우
#   작성일 : 2025.11.26

import math
import sys
input = sys.stdin.readline

def solve() :
    data = list(map(float, input().split()))
    x1, y1, r1, x2, y2, r2 = data
    
    d = math.dist((x1, y1), (x2, y2))
    
    if d >= r1 + r2 :
        print("0.000")
        return
    
    if d <= abs(r1 - r2) :
        print("{:.3f}".format(math.pi * min(r1, r2) ** 2))
        return
    
    theta1 = math.acos((r1 ** 2 + d ** 2 - r2 ** 2) / (2 * r1 * d))
    theta2 = math.acos((r2 ** 2 + d ** 2 - r1 ** 2) / (2 * r2 * d))
    
    s1 = (r1 ** 2 * theta1) - (r1 ** 2 * math.sin(2 * theta1) / 2)
    s2 = (r2 ** 2 * theta2) - (r2 ** 2 * math.sin(2 * theta2) / 2)
    
    result = s1 + s2
    print("{:.3f}".format(result))
    
solve()