import sys

def Fibbonacci(n):
    if n == 0:
        return 0
    elif n == 1:
        return 1
    return Fibbonacci(n - 1) + Fibbonacci(n - 2)

N = int(sys.stdin.readline())
print(Fibbonacci(N))