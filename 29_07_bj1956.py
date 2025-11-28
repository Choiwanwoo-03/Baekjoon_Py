#   작성자 : 컴퓨터공학부 최완우
#   작성일 : 2025.11.09

import sys
INF = int(1e9)

V, E = map(int, sys.stdin.readline().split())
my_map = [[INF] * V for _ in range(V)]
for _ in range(E):
    a, b, c = map(int, sys.stdin.readline().split())
    my_map[a-1][b-1] = c

for k in range(V):
    for i in range(V):
        for j in range(V):
            if my_map[i][j] > my_map[i][k] + my_map[k][j]:
                my_map[i][j] = my_map[i][k] + my_map[k][j]

answer = INF
for i in range(V):
    for j in range(V):
        answer = min(answer, my_map[i][j] + my_map[j][i])

if answer == INF:
    print('-1')
else:
    print(answer)