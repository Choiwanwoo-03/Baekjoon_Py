#   작성자 : 컴퓨터공학부 최완우
#   작성일 : 2025.11.26

import sys

input = sys.stdin.readline

def solve() :
    M = int(input())
    S = set()
    
    for _ in range(M) :
        command = input().split()
        
        if len(command) == 1:
            op = command[0]
            if op == "all" :
                S = set([i for i in range(1, 21)])
            elif op == "empty" :
                S = set()
            continue
        
        op = command[0]  
        x = int(command[1])
        
        if op == "add" :
            S.add(x)
        elif op == "remove" :
            S.discard(x)
        elif op == "check" :
            if x in S :
                print(1)
            else :
                print(0)
        elif op == "toggle" :
            if x in S :
                S.discard(x)
            else :
                S.add(x)
                
solve()