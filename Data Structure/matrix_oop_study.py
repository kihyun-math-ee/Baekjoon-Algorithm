import sys

class Matrix:
    """
    A class to represent a mathematical Matrix.
    Encapsulates grid data and matrix operations.
    """
    def __init__(self, matrix_data):
        self.data = matrix_data
        self.size = len(matrix_data)

    def __str__(self):
        return '\n'.join([' '.join(map(str, row)) for row in self.data])

    def plus(self, other):
        new_data = [[0] * self.size for _ in range(self.size)]
        for i in range(self.size):
            for j in range(self.size):
                new_data[i][j] = self.data[i][j] + other.data[i][j]
        return Matrix(new_data)
    
    def subtract(self, other):
        new_data = [[0] * self.size for _ in range(self.size)]
        for i in range(self.size):
            for j in range(self.size):
                new_data[i][j] = self.data[i][j] - other.data[i][j]
        return Matrix(new_data)
    
    def multiply(self, other):
        new_data = [[0] * self.size for _ in range(self.size)]
        for i in range(self.size):
            for j in range(self.size):
                for k in range(self.size):
                    new_data[i][j] += self.data[i][k] * other.data[k][j]
        return Matrix(new_data)
    
    def transpose(self):
        """
        Rotates the matrix 90 degrees over the diagonal.
        Logic: New[i][j] = Old[j][i]
        """
        new_data = [[0] * self.size for _ in range(self.size)]
        for i in range(self.size):
            for j in range(self.size):
                new_data[i][j] = self.data[j][i]
        return Matrix(new_data)

    def is_inverse_of(self, other):
        product_matrix = self.multiply(other)
        identity = [[1 if i == j else 0 for j in range(self.size)] for i in range(self.size)]
        
        if product_matrix.data == identity:
            return True
        else:
            return False

# --- Helper Function ---
def get_matrix_input(n):
    matrix = []
    for _ in range(n):
        matrix.append(list(map(int, sys.stdin.readline().split())))
    return matrix

# --- Main Execution ---
line = sys.stdin.readline().split()
if line:
    N = int(line[0])
    command = line[1]

    # Always read Matrix A
    matrix_A = Matrix(get_matrix_input(N))

    # Single Operand Commands
    if command == 'transpose':
        result = matrix_A.transpose()
        print("Transpose of Matrix:")
        print(result)

    # Double Operand Commands (Require Matrix B)
    else:
        matrix_B = Matrix(get_matrix_input(N))

        if command == 'plus':
            result = matrix_A.plus(matrix_B)
            print("Sum of Matrices:")
            print(result)

        elif command == 'subtract':
            result = matrix_A.subtract(matrix_B)
            print("Difference of Matrices:")
            print(result)

        elif command == 'multiply':
            result = matrix_A.multiply(matrix_B)
            print("Product of Matrices:")
            print(result)

        elif command == 'inverse_check':
            if matrix_A.is_inverse_of(matrix_B):
                print("The matrices are inverse to each other.")
            else:
                print("The matrices are NOT inverse.")