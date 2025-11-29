#   작성자 : 컴퓨터공학부 최완우
#   작성일 : 2025.11.12

from collections import deque

def bfs(start, target) :
    queue = deque()
    queue.append((start, ""))
    visited = [False] * 10000
    visited[start] = True

    while queue :
        num, command = queue.popleft()

        if num == target :
            return command

        d = (num * 2) % 10000
        if not visited[d] :
            visited[d] = True
            queue.append((d, command + "D"))

        s = (num - 1) % 10000
        if not visited[s] :
            visited[s] = True
            queue.append((s, command + "S"))

        l = (num % 1000) * 10 + num // 1000
        if not visited[l] :
            visited[l] = True
            queue.append((l, command + "L"))

        r = (num % 10) * 1000 + num // 10
        if not visited[r]:
            visited[r] = True
            queue.append((r, command + "R"))

def main() :
    import sys
    input = sys.stdin.readline
    t = int(input())
    for _ in range(t) :
        a, b = map(int, input().split())
        print(bfs(a, b))

if __name__ == "__main__" :
    main()