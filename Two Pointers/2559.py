import sys

N, K = map(int, sys.stdin.readline().split())
L = list(map(int, sys.stdin.readline().split()))

current_sum = sum(L[:K])
max_sum = current_sum

for i in range(K, N):
    current_sum = current_sum + L[i] - L[i - K]
    max_sum = max(max_sum, current_sum)

print(max_sum)