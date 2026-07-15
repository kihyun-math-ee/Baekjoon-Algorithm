import sys

n = int(sys.stdin.readline())
L = list(map(int, sys.stdin.readline().split()))
L = [0] + L
dp = [0] * (n + 1)

for i in range(1, n + 1):
    dp[i] = max(dp[i - 1] + L[i], L[i])

print(max(dp[1:]))