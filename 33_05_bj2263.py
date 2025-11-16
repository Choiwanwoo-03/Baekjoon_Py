#   작성자 : 컴퓨터공학부 최완우
#   작성일 : 2025.11.13

import sys
sys.setrecursionlimit(10 ** 6)
input = sys.stdin.readline

n = int(input())
inorder = list(map(int, input().split()))
postorder = list(map(int, input().split()))

index = [0] * (n + 1)
for i in range(n) :
    index[inorder[i]] = i
    
def preorder(in_start, in_end, post_start, post_end) :
    if in_start > in_end or post_start > post_end :
        return
    
    root = postorder[post_end]
    print(root, end = ' ')
    
    root_index = index[root]
    left_size = root_index - in_start
    
    preorder(in_start, root_index - 1, post_start, post_start + left_size - 1)
    
    preorder(root_index + 1, in_end, post_start + left_size, post_end - 1)
    
preorder(0, n - 1, 0, n - 1)