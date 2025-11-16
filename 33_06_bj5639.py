#   작성자 : 컴퓨터공학부 최완우
#   작성일 : 2025.11.16

import sys
sys.setrecursionlimit(10 ** 7)
input = sys.stdin.readline

preorder = []
while True :
    line = input().strip()
    if not line :
        break
    preorder.append(int(line))
    
def solve(start, end) :
    if start > end :
        return
    
    root = preorder[start]
    
    index = start + 1
    while index <= end and preorder[index] < root :
        index += 1
    
    solve(start + 1, index - 1)
    solve(index, end)
    print(root)
    
solve(0, len(preorder) - 1)