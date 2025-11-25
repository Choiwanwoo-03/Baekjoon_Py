#   작성자 : 컴퓨터공학부 최완우
#   작성일 : 2025.11.25

from itertools import permutations
import math

r = list(map(int, input().split()))

angle = [i * math.pi / 4 for i in range(8)]

def is_convex(arr):
    points = [(arr[i] * math.cos(angle[i]), arr[i] * math.sin(angle[i])) for i in range(8)]

    prev = 0
    for i in range(8):
        x1, y1 = points[i]
        x2, y2 = points[(i + 1) % 8]
        x3, y3 = points[(i + 2) % 8]

        cross = (x2 - x1) * (y3 - y2) - (y2 - y1) * (x3 - x2)

        if prev == 0:
            prev = cross
        else:
            if prev * cross < 0:
                return False
    return True

cnt = 0

for arr in permutations(r):
    if is_convex(arr):
        cnt += 1

print(cnt)