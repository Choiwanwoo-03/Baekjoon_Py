#   작성자 : 컴퓨터공학부 최완우
#   작성일 : 2025.11.25

def ccw(x1, y1, x2, y2, x3, y3):
    val = (x2 - x1) * (y3 - y1) - (y2 - y1) * (x3 - x1)
    if val > 0:
        return 1
    elif val < 0:
        return -1
    else:
        return 0

x1, y1, x2, y2 = map(int, input().split())
x3, y3, x4, y4 = map(int, input().split())

ccw1 = ccw(x1, y1, x2, y2, x3, y3)
ccw2 = ccw(x1, y1, x2, y2, x4, y4)
ccw3 = ccw(x3, y3, x4, y4, x1, y1)
ccw4 = ccw(x3, y3, x4, y4, x2, y2)

def solve():
    global x1, y1, x2, y2, x3, y3, x4, y4
    if ccw1 * ccw2 == 0 and ccw3 * ccw4 == 0:
        if (x2, y2) < (x1, y1):
            x1, y1, x2, y2 = x2, y2, x1, y1
        if (x4, y4) < (x3, y3):
            x3, y3, x4, y4 = x4, y4, x3, y3
        if (x3, y3) <= (x2, y2) and (x1, y1) <= (x4, y4):
            return 1
        else:
            return 0
    else:
        if ccw1 * ccw2 <= 0 and ccw3 * ccw4 <= 0:
            return 1
        else:
            return 0

print(solve())