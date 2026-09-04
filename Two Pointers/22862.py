import sys

N, K = map(int, sys.stdin.readline().split())
L = list(map(int, sys.stdin.readline().split()))
left = 0
right = 0
max_length = 0
current_length = 0
cnt = 0

while right <= N - 1 and left <= right:

    if L[right] % 2 == 0:
        current_length += 1
        right += 1

    elif L[right] % 2 == 1 and cnt < K:
        right += 1
        cnt += 1

    elif L[right] % 2 == 1 and cnt >= K:
        if L[left] % 2 == 1:
            cnt -= 1
        elif L[left] % 2 == 0:
            current_length -= 1
        left += 1

    if max_length < current_length:
        max_length = current_length

print(max_length)