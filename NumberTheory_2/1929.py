import sys
import math

def is_prime(n):
    limit = int(math.sqrt(n))

    if n < 2:
        return False
    
    else:
        for i in range(2, limit + 1):
            if n % i == 0:
                return False
            
        return True
    
M, N = map(int, sys.stdin.readline().split())
for num in range(M, N + 1):
    if is_prime(num):
        print(num)