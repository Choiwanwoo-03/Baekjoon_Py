#   작성자 : 컴퓨터공학부 최완우
#   작성일 : 2025.11.19

import sys
from collections import deque

def solve(n):
    dq = deque()
    turn = False
    for x in range(n, 0, -1) :
        if not turn:
            dq.append(x)
        else:
            dq.appendleft(x)
        turn = not turn

    print(*dq)

if __name__ == "__main__" :
    input = sys.stdin.readline
    n = int(input().strip())
    solve(n)
