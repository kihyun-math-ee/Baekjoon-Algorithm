import sys

target = []
def target_permutation(n, m, l):
    if len(target) == m:
        print(*target)
        return
    
    for i in range(n):
        if l[i] not in target:
            target.append(l[i])
            target_permutation(n, m, l)
            target.pop()

N, M = map(int, sys.stdin.readline().split())
L = list(map(int, sys.stdin.readline().split()))
L.sort()
target_permutation(N, M, L)