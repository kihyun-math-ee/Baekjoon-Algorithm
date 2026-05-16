import sys

N, M = map(int, sys.stdin.readline().split())
L = []
final_L = []

for i in range(N):
    rank = int(sys.stdin.readline())
    L.insert(rank - 1, i + 1)

L = L[:M]
L.reverse()

for idx in L:
    final_rank = int(sys.stdin.readline())
    final_L.insert(final_rank - 1, idx)

for j in range(3):
    print(final_L[j])
