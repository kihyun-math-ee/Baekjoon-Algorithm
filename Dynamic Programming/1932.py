import sys

N = int(sys.stdin.readline())
dp = ([[0 for _ in range(N)] for _ in range(N)])
target = []

for y in range(N):
    rows = list(map(int, sys.stdin.readline().split()))
    target.append(rows)

dp[0][0] = target[0][0]

for i in range(1, N):
    for j in range(i + 1):
        if j == 0:
            dp[i][j] = dp[i - 1][j] + target[i][j]
        elif j == i:
            dp[i][j] = dp[i - 1][j - 1] + target[i][j]
        else:
            dp[i][j] = max(dp[i - 1][j - 1] + target[i][j], dp[i - 1][j] + target[i][j])

print(max(dp[N - 1]))