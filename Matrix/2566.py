import sys
class Matrix:
    def __init__(self):
        self.matrix = []

    def add_row(self, row):
        self.matrix.append(row)

    def find_max(self):
        maximum = -1
        max_row = 0
        max_col = 0

        for i in range(9):
            for j in range(9):
                if self.matrix[i][j] > maximum:
                    maximum = self.matrix[i][j]
                    max_row = i + 1
                    max_col = j + 1
        print(maximum)
        print(max_row, max_col)

if __name__ == "__main__":
    my_matrix = Matrix()
    
    for i in range(9):
        row = list(map(int, sys.stdin.readline().split()))
        my_matrix.add_row(row)

    my_matrix.find_max()
