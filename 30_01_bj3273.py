#   작성자 : 컴퓨터공학부 최완우
#   작성일 : 2025.11.09

n = int(input())
a = sorted(map(int, input().split()))
x = int(input())

count = 0
left, right = 0, n - 1
while left < right:
    temp = a[left] + a[right]
    if temp == x:
        count += 1
        left += 1
        right -= 1
    elif temp < x:
        left += 1
    else:
        right -= 1
print(count)
