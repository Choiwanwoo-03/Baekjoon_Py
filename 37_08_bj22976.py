#   작성자 : 컴퓨터공학부 최완우
#   작성일 : 2025.11.20

import sys
input = sys.stdin.readline

n = int(input().strip())
existing = [tuple(map(int, input().split())) for _ in range(n - 1)]

if n <= 4 :
    total = n * (n - 1) // 2
    K = total - (n - 1)
    print(K)
    print(1)
    exist = set(existing)
    for i in range(1, n + 1) :
        for j in range(i + 1, n + 1) :
            if (i, j) not in exist and (j, i) not in exist :
                print(i, j)
                
else :
    add = []
    exist = set(existing)
    for i in range(2, n + 1) :
        if (1, i) not in exist and (i, 1) not in exist :
            add.append((1, i))
    K = len(add)
    print(K)
    print(2)
    for u, v in add :
        print(u, v)