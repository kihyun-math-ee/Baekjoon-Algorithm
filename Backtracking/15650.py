import sys

N, M = map(int, sys.stdin.readline().split())
L = []

def Combination_Sequence(start):
    if len(L) == M:
        print(*L)
        return
    
    for i in range(start, N + 1):
        L.append(i)

        Combination_Sequence(i + 1)
        L.pop()

Combination_Sequence(1)