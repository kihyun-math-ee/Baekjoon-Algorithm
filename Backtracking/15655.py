import sys

target = []
def target_combination(start, n, m, l):
    if len(target) == m:
        print(*target)
        return
    
    for i in range(start, n):
        target.append(l[i])
        target_combination(i + 1, n, m, l)
        target.pop()

N, M = map(int, sys.stdin.readline().split())
L = list(map(int, sys.stdin.readline().split()))
L.sort()
target_combination(0, N, M, L)