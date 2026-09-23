import sys

N = int(sys.stdin.readline())
factors = list(map(int, sys.stdin.readline().split()))
factors.sort()

if len(factors) == 1:
    print(factors[0] ** 2)

else:
    print(factors[0] * factors[-1])