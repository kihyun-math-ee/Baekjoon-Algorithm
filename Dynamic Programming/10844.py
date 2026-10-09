import sys

N = int(sys.stdin.readline())

dp = [[0] * 10 for _ in range(N)]
dp[0] = [0, 1, 1, 1, 1, 1, 1, 1, 1, 1]

for j in range(1, N):
    for k in range(0, 10):
        if k == 0:
            dp[j][k] = dp[j - 1][k + 1]
        elif k == 9:
            dp[j][k] = dp[j - 1][k - 1]
        else:
            dp[j][k] = dp[j - 1][k - 1] + dp[j - 1][k + 1]

print(sum(dp[N - 1]) % 1000000000)
