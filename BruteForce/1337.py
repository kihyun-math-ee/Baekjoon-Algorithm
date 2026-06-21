import sys

L = []
min_add = 5
N = int(sys.stdin.readline())
for _ in range(N):
    n = int(sys.stdin.readline())
    L.append(n)

L.sort()
i = 0
while True:
    if i < len(L):
        c = 0
        if L[i] in L:
            c += 1
        if L[i] + 1 in L:
            c += 1
        if L[i] + 2 in L:
            c += 1
        if L[i] + 3 in L:
            c += 1
        if L[i] + 4 in L:
            c += 1
        if 5 - c < min_add:
            min_add = 5 - c
        i += 1
    else:
        break
    