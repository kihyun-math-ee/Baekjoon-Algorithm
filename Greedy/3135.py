import sys

A, B = map(int, sys.stdin.readline().split())
N = int(sys.stdin.readline())
L = []
L.append(abs(A-B))

for _ in range(N):
    bookmark = int(sys.stdin.readline())
    L.append(abs(bookmark-B)+1)

L.sort()

print(L[0])