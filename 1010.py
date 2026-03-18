import sys

T = int(sys.stdin.readline())

for _ in range(T):
    N, M = map(int, sys.stdin.readline().split())
    permutation = 1
    factorial_N = 1
    
    for i in range(M - N + 1, M + 1):
        permutation *= i
    
    for j in range(1, N + 1):
        factorial_N *= j
    
    print(permutation // factorial_N)