import sys

N, M = map(int, sys.stdin.readline().split())
L = []

def Repeated_Permutation():
    global L

    if len(L) == M:
        print(*L)
        return
    
    for i in range(1, N + 1):
        L.append(i)
        Repeated_Permutation()
        L.pop()

Repeated_Permutation()     


