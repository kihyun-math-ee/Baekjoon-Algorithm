import sys
class Matrix:
    def __init__(self):
        self.matrix = []
        self.max_length = 0

    def add_row(self, row):
        self.matrix.append(list(row))

        if len(row) > self.max_length:
            self.max_length = len(row)


    def print_vertical(self):
        for j in range(self.max_length):
            for i in range(5):
                if j < len(self.matrix[i]):
                    print(self.matrix[i][j], end='')


if __name__ == "__main__":
    my_matrix = Matrix()
    for _ in range(5):
        row = sys.stdin.readline().strip()
        my_matrix.add_row(row)

    my_matrix.print_vertical()

                    