import sys
import math

def is_prime(n):
    limit = int(math.sqrt(n))
    
    if n < 2:
        return False
    
    for i in range(2, limit + 1):
        if n % i == 0:
            return False
        
    return True

prime_set = set()
for j in range(1, 246913):
    if is_prime(j):
        prime_set.add(j)

while True:
    N = int(sys.stdin.readline())
    cnt = 0
    
    if N == 0:
        sys.exit(0)

    for x in range(N + 1, 2*N + 1):
        if x in prime_set:
            cnt += 1

    print(cnt)
