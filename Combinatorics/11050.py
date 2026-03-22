import sys

N, K = map(int, sys.stdin.readline().split())
n = 1
k = 1
if K != 0:
    
    for i in range(K + 1, N + 1):
        n *= i
    
    for j in range(1, N - K + 1):
        k *= j

print(n//k)