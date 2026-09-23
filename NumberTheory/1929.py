import sys
import math

class All_Prime:
    def __init__(self):
        pass

    def is_prime(self, num):
        if num < 2:
            return False
        
        limit = int(math.sqrt(num))
        for i in range(2, limit + 1):
            if num % i == 0:
                return False
                
        return True
    
if __name__ == '__main__':
    my_all_prime = All_Prime()
    M, N = map(int, sys.stdin.readline().split())
    results = []

    for j in range(M, N + 1):
        if my_all_prime.is_prime(j):
            results.append(str(j))

    print('\n'.join(results))