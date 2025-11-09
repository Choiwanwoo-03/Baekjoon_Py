#   작성자 : 컴퓨터공학부 최완우
#   작성일 : 2025.11.09

import sys
input = sys.stdin.readline

n, s = map(int, input().split())
numbers = list(map(int, input().split()))

min_len = n + 1
left = 0
right = 0
current_sum = 0

while True :
    if current_sum >= s :
        min_len = min(min_len, right - left)
        current_sum -= numbers[left]
        left += 1
    elif right == n :
        break
    else :
        current_sum += numbers[right]
        right += 1

print(0 if min_len == n + 1 else min_len)
