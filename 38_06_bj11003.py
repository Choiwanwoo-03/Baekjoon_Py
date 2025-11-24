#   작성자 : 컴퓨터공학부 최완우
#   작성일 : 2025.11.24

import sys
from collections import deque
input = sys.stdin.readline

n, l = map(int, input().split())
arr = list(map(int, input().split()))

q = deque()

for i in range(n) :
    while q and q[-1][1] > arr[i] :
        q.pop()
    q.append((i, arr[i]))
    
    if q[0][0] < i - l + 1 :
        q.popleft()
    print(q[0][1], end= ' ')