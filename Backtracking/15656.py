import sys

target = []
def permutation_with_repetition(n, m, l):
    if len(target) == m:
        print(*target)
        return
    
    for i in range(n):
        target.append(l[i])
        permutation_with_repetition(n, m, l)
        target.pop()

N, M = map(int, sys.stdin.readline().split())
L = list(map(int, sys.stdin.readline().split()))
L.sort()
permutation_with_repetition(N, M, L)