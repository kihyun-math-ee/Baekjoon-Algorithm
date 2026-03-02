import sys
import math

class Findfraction:
    def __init__(self):
        None

    def findfunction(self, N):
        for i in range(math.floor((math.sqrt(2) * math.sqrt(N)) - 1), math.ceil((math.sqrt(2) * math.sqrt(N)) + 1)):
            
            if ((i - 1) * i) // 2 < N <= ((i) * (i + 1)) // 2:
                pos = N - ((i - 1) * i) // 2
                
                if i % 2 == 1:
                    print(f"{(i - pos) + 1}/{pos}")
                
                elif i % 2 == 0:
                    print(f"{pos}/{(i - pos) + 1}")


if __name__ == "__main__":
    my_findfraction = Findfraction()
    X = int(sys.stdin.readline())
    my_findfraction.findfunction(X)