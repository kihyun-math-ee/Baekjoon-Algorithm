import sys

N = int(sys.stdin.readline())
M = 1

if N == 0:
    print(1)

else:
    while N > 1:
        M *= N
        N = N - 1
    print(M)