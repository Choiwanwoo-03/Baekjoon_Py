#   작성자 : 컴퓨터공학부 최완우
#   작성일 : 2025.11.09

import sys
input = sys.stdin.readline

N = int(input())
is_prime = [True] * (N + 1)
is_prime[0] = is_prime[1] = False
for i in range(2, int(N ** 0.5) + 1) :
    if is_prime[i] :
        for j in range(i * i, N + 1, i) :
            is_prime[j] = False
primes = [i for i, val in enumerate(is_prime) if val]

count = 0
left, right = 0, 0
current_sum = 0
while True :
    if current_sum >= N :
        if current_sum == N :
            count += 1
        current_sum -= primes[left]
        left += 1
    elif right == len(primes) :
        break
    else:
        current_sum += primes[right]
        right += 1
print(count)
