#   작성자 : 컴퓨터공학부 최완우
#   작성일 : 2025.11.25

import sys
def input_word() :
    return list(map(int, sys.stdin.readline().split()))

p1 = input_word()
p2 = input_word()
p3 = input_word()

x1, y1 = p1[0], p1[1]
x2, y2 = p2[0], p2[1]
x3, y3 = p3[0], p3[1]

cross_product = (x2 - x1) * (y3 - y2) - (y2 - y1) * (x3 - x2)

if cross_product > 0 :
    print(1)
elif cross_product < 0 :
    print(-1)
else :
    print(0)