#   작성자 : 컴퓨터공학부 최완우
#   작성일 : 2025.11.23

import sys
input = sys.stdin.readline

s = input().rstrip()
bomb = input().rstrip()
b_len = len(bomb)

stack = []

for ch in s :
    stack.append(ch)
    
    if len(stack) >= b_len :
        if ''.join(stack[-b_len:]) == bomb :
            del stack[-b_len:]
            
result = ''.join(stack)
if result == '':
    print("FRULA")
else :
    print(result)