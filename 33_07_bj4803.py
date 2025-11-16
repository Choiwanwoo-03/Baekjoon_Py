#   작성자 : 컴퓨터공학부 최완우
#   작성일 : 2025.11.16

import sys
sys.setrecursionlimit(10 ** 9)
input = sys.stdin.readline

def dfs(node, parent) :
    global cycle
    visit[node] = True
    
    for i in graph[node] :
        if not visit[i] :
            dfs(i, node)
        elif i != parent :
            cycle = True
            
case = 1
while True :
    n, m = map(int, input().split())
    if n == 0 and m == 0 :
        break
    
    graph = [[] for _ in range(n + 1)]
    visit = [False] * (n + 1)
    
    for _ in range(m) :
        a, b = map(int, input().split())
        graph[a].append(b)
        graph[b].append(a)
        
    tree_count = 0
    for i in range(1, n + 1) :
        if not visit[i] :
            cycle = False
            dfs(i, -1)
            if not cycle :
                tree_count += 1
                
    if tree_count == 0 :
        print(f"Case {case}: No trees.")
    elif tree_count == 1 :
        print(f"Case {case}: There is one tree.")
    else :
        print(f"Case {case}: A forest of {tree_count} trees.")
        
    case += 1