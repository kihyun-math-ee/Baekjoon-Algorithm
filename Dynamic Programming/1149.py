import sys

N = int(sys.stdin.readline())
L = []
for _ in range(N):
    rows = list(map(int, sys.stdin.readline().split()))
    L.append(rows)

dp = [[0] * 3 for _ in range(N)]

dp[0][0] = L[0][0]
dp[0][1] = L[0][1]
dp[0][2] = L[0][2]

for i in range(1, N):
    dp[i][0] = min(dp[i - 1][1], dp[i - 1][2]) + L[i][0]
    dp[i][1] = min(dp[i - 1][0], dp[i - 1][2]) + L[i][1]
    dp[i][2] = min(dp[i - 1][0], dp[i - 1][1]) + L[i][2]

print(min(dp[N - 1]))