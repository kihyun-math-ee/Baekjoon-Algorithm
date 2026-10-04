import sys

N = int(sys.stdin.readline())
sequence = list(map(int, sys.stdin.readline().split()))
M = int(sys.stdin.readline())
sequence = [0] + sequence
prefix_sum = [0] * (N + 1)

for i in range(1, N + 1):
    prefix_sum[i] = prefix_sum[i - 1] + sequence[i]

for _ in range(M):
    left, right = map(int, sys.stdin.readline().split())
    print(prefix_sum[right] - prefix_sum[left - 1])