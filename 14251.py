import sys

L = sorted(list(map(int, sys.stdin.readline().split())))

if L[0] + L[1] > L[2]:
    print(sum(L))

else:
    print((L[0] + L[1]) + (L[0] + L[1] - 1))
    