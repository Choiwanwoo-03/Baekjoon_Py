#   작성자 : 컴퓨터공학부 최완우
#   작성일 : 2025.11.25

def ccw(x1, y1, x2, y2, x3, y3):
    val = (x2 - x1) * (y3 - y1) - (y2 - y1) * (x3 - x1)
    if val > 0:
        return 1
    elif val < 0:
        return -1
    return 0

x1, y1, x2, y2 = map(int, input().split())
x3, y3, x4, y4 = map(int, input().split())

p1 = (x1, y1)
p2 = (x2, y2)
p3 = (x3, y3)
p4 = (x4, y4)

ccw1 = ccw(*p1, *p2, *p3)
ccw2 = ccw(*p1, *p2, *p4)
ccw3 = ccw(*p3, *p4, *p1)
ccw4 = ccw(*p3, *p4, *p2)

intersect = False
collinear = False

if ccw1 * ccw2 == 0 and ccw3 * ccw4 == 0:
    if ccw1 == 0 and ccw2 == 0 and ccw3 == 0 and ccw4 == 0:
        a, b = p1, p2
        c, d = p3, p4
        if b < a:
            a, b = b, a
        if d < c:
            c, d = d, c

        if a <= d and c <= b:
            intersect = True
            collinear = True
    else:
        intersect = True

else:
    if ccw1 * ccw2 <= 0 and ccw3 * ccw4 <= 0:
        intersect = True

if not intersect:
    print(0)
    exit()

print(1)

if collinear:
    a, b = p1, p2
    c, d = p3, p4
    if b < a:
        a, b = b, a
    if d < c:
        c, d = d, c

    start = max(a, c)
    end = min(b, d)

    if start == end:
        print(start[0], start[1])

else:
    A = x1 * y2 - y1 * x2
    B = x3 * y4 - y3 * x4
    den = (x1 - x2) * (y3 - y4) - (y1 - y2) * (x3 - x4)

    px = (A * (x3 - x4) - (x1 - x2) * B) / den
    py = (A * (y3 - y4) - (y1 - y2) * B) / den

    if abs(px - round(px)) < 1e-9:
        px = round(px)
    if abs(py - round(py)) < 1e-9:
        py = round(py)

    print(px, py)