#   작성자 : 컴퓨터공학부 최완우
#   작성일 : 2025.11.12

from collections import deque
import sys

def solve_correct():
    input_data = sys.stdin.read().split()
    if not input_data:
        return

    T = int(input_data[0])
    data_index = 1
    MAX = 10000

    for _ in range(T):
        A = int(input_data[data_index])
        B = int(input_data[data_index + 1])
        data_index += 2
        
        parent = [None] * MAX 
        
        queue = deque([A])
        parent[A] = (A, "")
        while queue:
            current_num = queue.popleft()
            
            if current_num == B:
                route = []
                temp_num = B
                
                while temp_num != A:
                    prev_num, cmd = parent[temp_num]
                    route.append(cmd)
                    temp_num = prev_num
                
                print("".join(route[::-1]))
                break

            next_num = (2 * current_num) % MAX
            if parent[next_num] is None:
                parent[next_num] = (current_num, "D")
                queue.append(next_num)

            next_num = current_num - 1 if current_num != 0 else 9999
            if parent[next_num] is None:
                parent[next_num] = (current_num, "S")
                queue.append(next_num)

            next_num = (current_num % 1000) * 10 + (current_num // 1000)
            if parent[next_num] is None:
                parent[next_num] = (current_num, "L")
                queue.append(next_num)

            next_num = (current_num % 10) * 1000 + (current_num // 10)
            if parent[next_num] is None:
                parent[next_num] = (current_num, "R")
                queue.append(next_num)

solve_correct()