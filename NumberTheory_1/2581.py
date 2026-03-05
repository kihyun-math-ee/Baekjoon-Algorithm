import sys

class Find_Prime:
    def __init__(self):
        self.prime_set = set()

    def boundary(self, leftend, rightend):
        for i in range(leftend, rightend + 1):
            if i < 2:
                continue
                
            for j in range(2, i):
                if i % j == 0:
                    break
            else:
                self.prime_set.add(i)

        if not self.prime_set:
            print(-1)
        else:
            print(sum(self.prime_set))
            print(min(self.prime_set))

if __name__ == "__main__":
    my_find_prime = Find_Prime()
    M = int(sys.stdin.readline())
    N = int(sys.stdin.readline())
    my_find_prime.boundary(M, N)