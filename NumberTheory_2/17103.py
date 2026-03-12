import sys

MAX_N = 1000000
primes = [True] * (MAX_N + 1)
primes[0] = False
primes[1] = False

for i in range(2, 1001):
    if primes[i]:
        for multiple in range(i * 2, MAX_N + 1, i):
            primes[multiple] = False

T = int(sys.stdin.readline())

for _ in range(T):
    N = int(sys.stdin.readline())
    cnt = 0
    median = N // 2
    
    for j in range(2, median + 1):
        if primes[j] == True and primes[N - j] == True:
            cnt += 1
    
    print(cnt)
