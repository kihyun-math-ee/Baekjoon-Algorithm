import sys
from collections import deque

N = int(sys.stdin.readline())
L = []
cnt = 0

target = int(sys.stdin.readline())

for _ in range(N-1):
    V = int(sys.stdin.readline())
    L.append(V)

if L:
    while target <= max(L):
        idx = L.index(max(L))
        target += 1
        L[idx] -= 1
        cnt += 1

print(cnt)
