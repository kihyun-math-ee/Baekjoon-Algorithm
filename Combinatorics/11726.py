import sys
import math

n = int(sys.stdin.readline())
S = 0

for h in range((n // 2) + 1):
    v = n - (2 * h)

    S += math.comb(h + v, h)

print(S % 10007)