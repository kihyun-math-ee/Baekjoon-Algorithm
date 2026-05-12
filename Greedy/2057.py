import sys

def factorial(n):
    if n == 0:
        return 1
    else:
        return n * factorial(n-1)

L = []
N = int(sys.stdin.readline())
p = 0

for i in range(21):
    L.append(factorial(i))

L.reverse()

if N == 0:
    print('NO')
    sys.exit(0)
else:
    while (N > 0) and p <= 20:
        while L[p] > N:
            p += 1
        N -= L[p]
        p += 1
    if N == 0:
        print('YES')

    else:
        print('NO')