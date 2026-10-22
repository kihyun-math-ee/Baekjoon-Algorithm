import sys

max_size = 1000001
L = [0] * (max_size)

N, K = map(int, sys.stdin.readline().split())

for _ in range(N):
    g, x = map(int, sys.stdin.readline().split())
    L[x] = g

step = (2 * K) + 1
current_sum = sum(L[:step])
max_sum = current_sum


for i in range(step, max_size):
    current_sum = current_sum + L[i] - L[i - step]

    if current_sum > max_sum:
        max_sum = current_sum

print(max_sum)