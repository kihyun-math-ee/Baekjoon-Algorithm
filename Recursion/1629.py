import sys

def power(a, b, c):
    if b == 0:
        return 1
    
    half = power(a, b // 2 ,c)

    if b % 2 == 0:
        return (half * half) % c
    
    else:
        return (half * half % c) * a % c
    
A, B, C = map(int, sys.stdin.readline().split())
print(power(A, B, C))