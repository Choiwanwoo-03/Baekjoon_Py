#   작성자 : 컴퓨터공학부 최완우
#   작성일 : 2025.11.24

import sys
input = sys.stdin.readline

n = int(input().strip())
points = [tuple(map(int, input().split())) for _ in range(n)]

area = 0

for i in range(n) :
    x1, y1 = points[i]
    x2, y2 = points[(i + 1) % n]
    area += (x1 * y2) - (x2 * y1)

print(abs(area) / 2)