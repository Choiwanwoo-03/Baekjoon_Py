#   작성자 : 컴퓨터공학부 최완우
#   작성일 : 2025.11.26

import sys
input = sys.stdin.readline

def solve() :
    N = int(input())
    poly = []
    for _ in range(N) :
        poly.append(list(map(int, input().split())))
        
    def segment(p, a, b) :
        if min(a[0], b[0]) <= p[0] <= max(a[0], b[0]) and \
            min(a[1], b[1]) <= p[1] <= max(a[1], b[1]) :
            
                if(a[0] - p[0]) * (b[1] - p[1]) - (a[1] - p[1]) * (b[0] - p[0]) == 0 :
                    return True
        return False

    def check(p) :
        x, y = p
        cnt = 0
    
        for i in range(N) :
            x1, y1 = poly[i]
            x2, y2 = poly[(i + 1) % N]
        
            if segment(p, (x1, y1), (x2, y2)) :
                return 1
        
            if (y1 > y) != (y2 > y) :
                intersect_x = (x2 - x1) * (y - y1) / (y2 - y1) + x1
            
                if x < intersect_x :
                    cnt += 1
                
        return 1 if cnt % 2 == 1 else 0
    for _ in range(3) :
        p = list(map(int, input().split()))
        print(check(p))
        
solve()