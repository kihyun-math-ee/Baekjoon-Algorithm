import sys

candidate = []
is_first = True

def lottery(start, l):
    if len(candidate) == 6:
        print(*candidate)
        return
    
    for i in range(start, l[0] + 1):
        candidate.append(l[i])
        lottery(i + 1, l)
        candidate.pop()

while True:
    L = list(map(int, sys.stdin.readline().split()))
    
    if L[0] == 0:
        break
    
    if not is_first:
        print()
    is_first = False

    lottery(1, L)        