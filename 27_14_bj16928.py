#   작성자 : 컴퓨터공학부 최완우
#   작성일 : 2025.11.06

import sys
from collections import deque
input = sys.stdin.readline

N, M = map(int, input().split())
move = dict()
for _ in range(N) :
    x, y = map(int, input().split())
    move[x] = y
for _ in range(M) :
    u, v = map(int, input().split())
    move[u] = v

visited = [False] * 101
board = [0] * 101
queue = deque()
queue.append(1)
visited[1] = True

while queue :
    pos = queue.popleft()
    for dice in range(1, 7) :
        nxt = pos + dice
        if nxt > 100 :
            continue
        if nxt in move :
            nxt = move[nxt]
        if not visited[nxt] :
            visited[nxt] = True
            board[nxt] = board[pos] + 1
            queue.append(nxt)
print(board[100])