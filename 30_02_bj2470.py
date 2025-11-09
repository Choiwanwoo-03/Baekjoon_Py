#   작성자 : 컴퓨터공학부 최완우
#   작성일 : 2025.11.09

import sys
input = sys.stdin.readline

n = int(input())
li = sorted(map(int, input().split()))
left, right = 0, n-1
mini = 2_000_000_001
answer = (0, 0)

while left < right :
    s = li[left] + li[right]
    if abs(s) < mini :
        mini = abs(s)
        answer = (li[left], li[right])
    if s < 0 :
        left += 1
    else :
        right -= 1
print(*answer)
