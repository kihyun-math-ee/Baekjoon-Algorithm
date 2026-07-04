import sys

N = int(sys.stdin.readline())
dp = [0] * N
L = []

for i in range(N):
    v = int(sys.stdin.readline())
    L.append(v)

dp[0] = L[0]
if N >= 2:
    dp[1] = dp[0] + L[1]
    if N >= 3:
        dp[2] = max(L[0] + L[1], L[0] + L[2], L[1] + L[2])
        if N >= 4:
            for i in range(3, N):
                dp[i] = max(dp[i - 3] + L[i - 1] + L[i], dp[i - 2] + L[i], dp[i - 1])

print(dp[N - 1])