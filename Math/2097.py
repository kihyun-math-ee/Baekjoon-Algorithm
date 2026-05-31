import sys
import math

N = int(sys.stdin.readline())
k = int(math.sqrt(N))

if N <= 4:
    print(4)
    sys.exit(0)

elif N <= k * k:
    W = k
    H = k

elif k * k < N <= k * (k + 1):
    W = k
    H = k + 1

else:
    W = k + 1
    H = k + 1

print(2 * (W - 1 + H - 1))