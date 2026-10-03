import sys

N = int(sys.stdin.readline())
A = list(map(int, sys.stdin.readline().split()))
dp = [0] * N
dp = A.copy()

for i in range(0, N):
    for j in range(i):
        if A[j] < A[i]:
            dp[i] = max((dp[j] + A[i]), dp[i])

print(max(dp))