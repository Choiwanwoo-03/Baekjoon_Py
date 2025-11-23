#   작성자 : 컴퓨터공학부 최완우
#   작성일 : 2025.11.23

import sys
input = sys.stdin.readline

N = int(input())
h = [int(input()) for _ in range(N)]

stack = []
max_area = 0

for i in range(N) :
    while stack and h[stack[-1]] > h[i] :
        height = h[stack.pop()]
        width = i if not stack else i - stack[-1] -1
        max_area = max(max_area, height * width)
    stack.append(i)
    
while stack :
    height = h[stack.pop()]
    width = N if not stack else N - stack[-1] -1
    max_area = max(max_area, height * width)
    
print(max_area)