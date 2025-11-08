#   작성자 : 컴퓨터공학부 최완우
#   작성일 : 2025.11.08

from collections import deque
import sys
input = sys.stdin.readline

N, K = map(int, input().split())
time = [-1] * 100001
queue = deque()
queue.append(N)
time[N] = 0
while queue :
    x = queue.popleft()
    if x == K :
        print(time[x])
        break
    if 0 < x * 2 < 100001 and time[x * 2] == -1 :
        time[x * 2] = time[x]
        queue.appendleft(x * 2)
    for nx in [x - 1, x + 1] :
        if 0 <= nx < 100001 and time[nx] == -1 :
            time[nx] = time[x] + 1
            queue.append(nx)