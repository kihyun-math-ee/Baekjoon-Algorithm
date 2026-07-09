import sys

max_N = 10000
dp = [0] * (max_N + 1)
dp[0] = 1

for i in range(1, max_N + 1):
    for k in range((i // 2) + 1):
        dp[i] += dp[k]

T = int(sys.stdin.readline())

for _ in range(T):
    N = int(sys.stdin.readline())
    print(dp[N])
