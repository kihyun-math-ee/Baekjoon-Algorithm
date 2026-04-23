import sys

A, B, N = map(int, sys.stdin.readline().split())
L = []
target = A % B

for i in range(N):
    target *= 10
    L.append(target // B)
    target = target % B

print(L[N-1])

