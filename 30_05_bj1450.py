#   작성자 : 컴퓨터공학부 최완우
#   작성일 : 2025.11.10

from itertools import combinations
import bisect
import sys
input = sys.stdin.readline

N, C = map(int, input().split())
arr = list(map(int, input().split()))

left = arr[:N // 2]
right = arr[N // 2:]

sub_left = []
for i in range(len(left) + 1) :
    for comb in combinations(left, i) :
        sub_left.append(sum(comb))
sub_left.sort()

sub_right = []
for i in range(len(right) + 1) :
    for comb in combinations(right, i) :
        sub_right.append(sum(comb))
        
answer = 0
for i in sub_right :
    if i > C :
        continue
    remain = C - i
    idx = bisect.bisect_right(sub_left, remain)
    answer += idx

print(answer)