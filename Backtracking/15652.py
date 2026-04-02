import sys

N, M = map(int, sys.stdin.readline().split())
L = []

def Repeated_Combination(start):
    if len(L) == M:
        print(*L)
        return
    
    for i in range(start, N + 1):
        L.append(i)
        
        Repeated_Combination(i)
        L.pop()

Repeated_Combination(1)