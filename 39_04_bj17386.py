#   작성자 : 컴퓨터공학부 최완우
#   작성일 : 2025.11.25

def ccw(x1, y1, x2, y2, x3, y3):
    return (x2 - x1) * (y3 - y1) - (y2 - y1) * (x3 - x1)

x1, y1, x2, y2 = map(int, input().split())
x3, y3, x4, y4 = map(int, input().split())

res1 = ccw(x1, y1, x2, y2, x3, y3)
res2 = ccw(x1, y1, x2, y2, x4, y4)
res3 = ccw(x3, y3, x4, y4, x1, y1)
res4 = ccw(x3, y3, x4, y4, x2, y2)

if res1 * res2 < 0 and res3 * res4 < 0:
    print(1)
else:
    print(0)
