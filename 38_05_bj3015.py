#   작성자 : 컴퓨터공학부 최완우
#   작성일 : 2025.11.24

import sys
input = sys.stdin.readline

n = int(input())
stack = []
result = 0

for _ in range(n) :
    current_height = int(input())
    count = 1
    
    while stack and stack[-1][0] < current_height :
        result += stack.pop()[1]
        
    if stack and stack[-1][0] == current_height :
        count = stack.pop()[1]
        result += count
        
        if stack :
            result += 1
        stack.append((current_height, count + 1))
        
    else :
        if stack : 
            result += 1
        stack.append((current_height, 1))
        
print(result)