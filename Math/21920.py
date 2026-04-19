import sys
import math

N = int(sys.stdin.readline())
sequence = list(map(int, sys.stdin.readline().split()))
X = int(sys.stdin.readline())
num = 0
total_sum = 0

for i in range(N):
    if math.gcd(sequence[i], X) == 1:
        num += 1
        total_sum += sequence[i]

M = sum(total_sum) / num
print(M)
