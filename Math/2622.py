import sys
import math

N = int(sys.stdin.readline())
cnt = 0

for a in range(1, (N // 2) + 1):
    min_b = math.ceil((N-a) / 2)
    max_b = a
    if max_b >= min_b:
        cnt += (max_b - min_b + 1)

print(cnt)    