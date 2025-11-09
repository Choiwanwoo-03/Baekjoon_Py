#   작성자 : 컴퓨터공학부 최완우
#   작성일 : 2025.11.09

import sys
input = sys.stdin.readline

n = int(input())
m = int(input())

inf = 10 ** 9
dist = [[inf] * (n + 1) for _ in range(n + 1)]

for i in range(1, n + 1) :
    dist[i][i] = 0
    
for _ in range(m) :
    a, b, c = map(int, input().split())
    if c < dist[a][b] :
        dist[a][b] = c
        
for k in range(1, n + 1) :
    for i in range(1, n + 1) :
        for j in range(1, n + 1) :
            if dist[i][j] > dist[i][k] + dist[k][j] :
                dist[i][j] = dist[i][k] + dist[k][j]
                
for i in range(1, n + 1) :
    for j in range(1, n + 1) :
        print(0 if dist[i][j] == inf else dist[i][j], end = " ")
    print()