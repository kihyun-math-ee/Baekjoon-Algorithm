import sys
class Matrix:
    def __init__(self):
        self.matrix =[[0] * 101 for _ in range(101)] # for evading index error
        self.area = 0

    def pixel(self, a, b):

        for i in range(a, a + 10):
            for j in range(b, b + 10):
                if self.matrix[i][j] == 0:
                    self.matrix[i][j] = 1
                    self.area += 1


    def result(self):
        print(self.area)
    
if __name__ == "__main__":
    N = int(sys.stdin.readline())
    my_matrix = Matrix()
    for _ in range(N):
        a, b = map(int, sys.stdin.readline().split())
        my_matrix.pixel(a, b)

    my_matrix.result()

        
