#   작성자 : 컴퓨터공학부 최완우
#   작성일 : 2025.11.17

import sys
input = sys.stdin.read
data = input().split()

T = int(data[0])
index = 1

for _ in range(T):
    N = int(data[index])
    M = int(data[index + 1]) 
    index += 2
    
    for i in range(M) :
        index += 2
    
    print(N - 1)