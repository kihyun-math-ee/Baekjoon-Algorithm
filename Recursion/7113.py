import sys

def square(n, m):
    if n == m:
        return 1
    elif n > m:
        return 1 + square(n - m, m)
    elif n < m:
        return 1 + square(n, m - n)

N, M = map(int, sys.stdin.readline().split())
print(square(N, M))