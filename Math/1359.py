import sys
import math

N, M, K = map(int, sys.stdin.readline().split())
S = 0
for i in range(K, M + 1):
    S += math.comb(M, i)*math.comb(N-M, M-i)

P = S/math.comb(N, M)
print(P)
