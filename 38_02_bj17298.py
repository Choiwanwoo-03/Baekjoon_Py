#   작성자 : 컴퓨터공학부 최완우
#   작성일 : 2025.11.23

import sys
input = sys.stdin.readline

N = int(input())
arr = list(map(int, input().split()))
answer = [-1] * N
stack = []

for i in range(N) :
    while stack and arr[stack[-1]] < arr[i] :
        idx = stack.pop()
        answer[idx] = arr[i]
    stack.append(i)
    
print(*answer)