import sys

N, M = map(int, sys.stdin.readline().split())
L = list(map(int, sys.stdin.readline().split()))

left, right = 0, 0
current_sum = 0
cnt = 0

while True:

    if current_sum >= M:
        if current_sum == M:
            cnt += 1
        current_sum -= L[left]
        left += 1

    elif right == N:
        break

    else:
        current_sum += L[right]
        right += 1

print(cnt)