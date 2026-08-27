import sys

N = int(sys.stdin.readline())
dp = [0] * (N)
L = []

for _ in range(N):
    x = float(sys.stdin.readline())
    L.append(x)

dp[0] = L[0]
for i in range(1, N):
    dp[i] = max(dp[i - 1] * L[i], L[i])

print(f'{max(dp):.3f}')