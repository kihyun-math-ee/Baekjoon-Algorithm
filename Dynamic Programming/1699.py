import sys
import math

N = int(sys.stdin.readline())
dp = [0] * (N + 1)

for i in range(1, N + 1):
    min_result = float('inf')
    for j in range(1, int(math.sqrt(i)) + 1):
        if min_result > dp[i - (j ** 2)]:
            min_result = dp[i - (j ** 2)]
    dp[i] = min_result + 1

print(dp[N])