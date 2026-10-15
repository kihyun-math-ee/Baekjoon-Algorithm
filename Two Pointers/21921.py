import sys

N, X = map(int, sys.stdin.readline().split())
L = list(map(int, sys.stdin.readline().split()))

current_sum = sum(L[:X])
max_sum = current_sum
cnt = 1

for i in range(X, N):
    current_sum = current_sum + L[i] - L[i - X]

    if max_sum < current_sum:
        max_sum = current_sum
        cnt = 1

    elif max_sum == current_sum:
        cnt += 1

if max_sum == 0:
    print('SAD')

else:
    print(max_sum)
    print(cnt)