import sys
import math

target = []
N, F = map(int, sys.stdin.readline().split())
L = list(range(1, N + 1))

def permutation():
    if len(target) == N:
        pascal()
        return

    for i in range(1, N + 1):
        if i not in target:
            target.append(i)
            permutation()
            target.pop()

def pascal():
    s = 0
    for j in range(N):
        s += math.comb(N - 1, j) * target[j]
    if s == F:
        print(*target)
        sys.exit(0)
    return

permutation()