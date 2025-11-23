#   작성자 : 컴퓨터공학부 최완우
#   작성일 : 2025.11.23

import sys
sys.setrecursionlimit(10 ** 7)
input = sys.stdin.readline

k = int(input().strip())
x, y = map(int, input().split())
n = 1 << k

board = [[0] * n for _ in range(n)]
board[n - y][x - 1] = -1

tile_id = 1

def is_empty(sx, sy, size) :
    for i in range(sx, sx + size) :
        for j in range(sy, sy + size) :
            if board[i][j] != 0 :
                return False
    return True

def tromino(sx, sy, size, hole_x, hole_y) :
    global tile_id

    if size == 1 :
        return

    half = size // 2

    if hole_x < sx + half :
        if hole_y < sy + half :
            hole_quad = 0
        else:
            hole_quad = 2
    else:
        if hole_y < sy + half :
            hole_quad = 1
        else:
            hole_quad = 3

    centers = [
        (sx + half - 1, sy + half - 1),
        (sx + half,     sy + half - 1),
        (sx + half - 1, sy + half),
        (sx + half,     sy + half)
    ]
    for quad in range(4):
        if quad != hole_quad :
            cx, cy = centers[quad]
            board[cx][cy] = tile_id
    tile_id += 1

    quads = [
        (sx, sy),
        (sx + half, sy),
        (sx, sy + half),
        (sx + half, sy + half)
    ]
    for quad in range(4):
        qx, qy = quads[quad]
        if quad == hole_quad:
            tromino(qx, qy, half, hole_x, hole_y)
        else:
            cx, cy = centers[quad]
            tromino(qx, qy, half, cx, cy)

tromino(0, 0, n, n - y, x - 1)

for row in board:
    print(" ".join(map(str, row)))