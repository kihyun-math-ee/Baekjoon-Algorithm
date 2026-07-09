import sys
import math

N = int(sys.stdin.readline())
line = list(map(int, sys.stdin.readline().split()))
S = 0
dp = [0] * (N + 1)

for j in range(1, N + 1):
    dp[j] = dp[j - 1] + line[j - 1]

for i in range(N):
    S += line[i] * (dp[-1] - dp[i + 1])

print(S)

