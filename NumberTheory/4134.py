import sys
import math

class Prime:
    def __init__(self):
        pass

    def is_prime(self, num):
        self.limit = int(math.sqrt(num))

        if num < 2:
            return False
        
        else:
            for i in range(2, self.limit + 1):
                if num % i == 0:
                    return False
            
            return True
        
if __name__ == "__main__":
    my_prime = Prime()
    T = int(sys.stdin.readline())
    
    for _ in range(T):
        n = int(sys.stdin.readline())
        
        while not my_prime.is_prime(n):
            n += 1
        
        print(n)
        