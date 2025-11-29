#   작성자 : 컴퓨터공학부 최완우
#   작성일 : 2025.11.24

import sys
from collections import deque

input = sys.stdin.readline
INF = -10**18

N, M, C, D = map(int, input().split())
b = list(map(int, input().split()))

dp_prev = [0] * (M + 1)

b0 = b[0]
for k in range(1, M + 1):
    dp_prev[k] = M - abs(b0 - k)

groups = []
for r in range(C):
    start = C if r == 0 else r
    if start > M:
        break
    arr = []
    k = start
    while k <= M:
        arr.append(k)
        k += C
    if arr:
        groups.append(arr)

W = D // C if C != 0 else 0
max_len = max(len(g) for g in groups)

vals = [0] * max_len
L = [0] * max_len
R = [0] * max_len

for t in range(1, N):
    dp_curr = [INF] * (M + 1)
    bt = b[t]

    for temps in groups:
        n = len(temps)

        for i in range(n):
            vals[i] = dp_prev[temps[i]]

        if W >= n:
            best = max(vals[:n])
            if best <= INF + 1:
                continue
            for i in range(n):
                ktemp = temps[i]
                dp_curr[ktemp] = best + (M - abs(bt - ktemp))
            continue

        dq = deque()
        for j in range(n):
            limit = j - W
            while dq and dq[0] < limit:
                dq.popleft()
            while dq and vals[dq[-1]] <= vals[j]:
                dq.pop()
            dq.append(j)
            L[j] = vals[dq[0]]

        dq.clear()
        for j in range(n - 1, -1, -1):
            limit = j + W
            while dq and dq[0] > limit:
                dq.popleft()
            while dq and vals[dq[-1]] <= vals[j]:
                dq.pop()
            dq.append(j)
            R[j] = vals[dq[0]]

        for i in range(n):
            best_prev = max(L[i], R[i])
            if best_prev <= INF + 1:
                continue
            ktemp = temps[i]
            dp_curr[ktemp] = best_prev + (M - abs(bt - ktemp))

    dp_prev = dp_curr

ans = max(dp_prev[1:])
print(ans if ans > 0 else 0)