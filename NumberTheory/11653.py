import sys

class Factorization:
    def __init__(self):
        pass

    def Factorize_num(self, number):
        if number == 1:
            return 
            
        i = 2
        
        while 1 < number:
            while number % i == 0:
                print(i) 
                number = number // i
            i += 1

if __name__ == "__main__":
    my_factorization = Factorization()
    N = int(sys.stdin.readline())
    my_factorization.Factorize_num(N)

