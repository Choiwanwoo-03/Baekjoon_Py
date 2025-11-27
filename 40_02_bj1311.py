#   작성자 : 컴퓨터공학부 최완우
#   작성일 : 2025.11.27

import sys
input = sys.stdin.readline

INF = 10**15

def hungarian(a):
    n = len(a)
    m = len(a[0])
    u = [0] * (n + 1)
    v = [0] * (m + 1)
    p = [0] * (m + 1)
    way = [0] * (m + 1)

    for i in range(1, n + 1):
        p[0] = i
        j0 = 0
        minv = [INF] * (m + 1)
        used = [False] * (m + 1)
        while True:
            used[j0] = True
            i0 = p[j0]
            delta = INF
            j1 = 0
            for j in range(1, m + 1):
                if not used[j]:
                    cur = a[i0 - 1][j - 1] - u[i0] - v[j]
                    if cur < minv[j]:
                        minv[j] = cur
                        way[j] = j0
                    if minv[j] < delta:
                        delta = minv[j]
                        j1 = j
            for j in range(0, m + 1):
                if used[j]:
                    u[p[j]] += delta
                    v[j] -= delta
                else:
                    minv[j] -= delta
            j0 = j1
            if p[j0] == 0:
                break

        while True:
            j1 = way[j0]
            p[j0] = p[j1]
            j0 = j1
            if j0 == 0:
                break

    matching_cost = 0
    for j in range(1, m + 1):
        matching_cost += a[p[j] - 1][j - 1]
    return matching_cost

def main():
    N = int(input())
    cost = [list(map(int, input().split())) for _ in range(N)]
    print(hungarian(cost))


if __name__ == "__main__":
    main()
