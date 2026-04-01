import sys

L = []
N, M = map(int, sys.stdin.readline().split())

def Permutation_Sequence():
    global L

    if len(L) == M:
        print(*L)
        return
    

    for i in range(1, N + 1):
        if i not in L:
            L.append(i)
            Permutation_Sequence()
            L.pop()

Permutation_Sequence()

        


