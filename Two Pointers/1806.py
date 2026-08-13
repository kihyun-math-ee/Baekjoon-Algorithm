import sys

N, S = map(int, sys.stdin.readline().split())
L = list(map(int, sys.stdin.readline().split()))

left = 0
right = 0
current_sum = 0
min_length = float('inf')

while True:

    if current_sum < S:
        if right == N:
            break
        else:
            current_sum += L[right]
            right += 1

    else:
        if right - left < min_length:
            min_length = right - left

        current_sum -= L[left]
        left += 1

if min_length == float('inf'):
    print(0)

else:
    print(min_length)