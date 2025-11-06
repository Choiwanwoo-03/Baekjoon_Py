#   작성자 : 컴퓨터공학부 최완우
#   작성일 : 2025.11.06

import sys
from collections import deque
input = sys.stdin.readline

def solve(L, start, end) :
    dx = [1, 2, 2, 1, -1, -2, -2, -1]
    dy = [2, 1, -1, -2, -2, -1, 1, 2]
    visit = [[False] * L for _ in range(L)]
    queue = deque()
    queue.append((start[0], start[1], 0))
    visit[start[0]][start[1]] = True
    
    while queue :
        x, y, cnt = queue.popleft()
        if(x, y) == end :
            return cnt
        for i in range(8) :
            nx, ny = x + dx[i], y + dy[i]
            if 0 <= nx < L and 0 <= ny < L and not visit[nx][ny] :
                visit[nx][ny] = True
                queue.append((nx, ny, cnt + 1))
    return -1

T = int(input())
for _ in range(T) :
    L = int(input())
    sx, sy = map(int, input().split())
    ex, ey = map(int, input().split())
    print(solve(L, (sx, sy), (ex, ey)))