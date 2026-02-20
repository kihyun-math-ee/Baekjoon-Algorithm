import sys
N = int(sys.stdin.readline())
factors = []

if N == 1:
    print()

else:
    i = 2
    while N > 1:
        while N % i == 0:
            factors.append(i)
            N = N // i
        i += 1

    print(*factors, sep="\n")
