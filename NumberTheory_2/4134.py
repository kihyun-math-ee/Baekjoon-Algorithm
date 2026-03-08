import sys
import math

def is_prime(num):
    if num < 2:
        return False

    limit = int(math.sqrt(num))
    for i in range(2, limit + 1):
        if num % i == 0:
            return False
            
    return True

T = int(sys.stdin.readline())

for _ in range(T):
    n = int(sys.stdin.readline())
    while not is_prime(n):
        n += 1

    print(n)
        