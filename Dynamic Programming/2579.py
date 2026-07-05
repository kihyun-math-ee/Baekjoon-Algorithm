import sys

N = int(sys.stdin.readline())
dp = [0] * 300
target = []

for _ in range(N):
    score = int(sys.stdin.readline())
    target.append(score)

dp[0] = target[0]

if N >= 2:
    dp[1] = target[0] + target[1]
    if N >= 3:
        dp[2] = max(target[0] + target[2], target[1] + target[2])

for i in range(3, N):
    dp[i] = max(dp[i - 2] + target[i], dp[i - 3] + target[i - 1] + target[i]) 

print(dp[N -1])