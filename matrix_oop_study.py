import sys

class Matrix:
    """
    A class to represent a mathematical Matrix.
    Encapsulates grid data and matrix operations (Addition, Multiplication).
    """
    def __init__(self, matrix_data):
        # Store the raw 2D list (grid)
        self.data = matrix_data
        # Assume square matrix (NxN) for this problem
        self.size = len(matrix_data)

    def __str__(self):
        """
        Magic Method: String Representation.
        Allows us to use 'print(matrix_object)' directly.
        Converts the 2D list into a clean, formatted string.
        """
        # 1. Convert numbers to strings (map(str, row))
        # 2. Join numbers with space (' '.join(...))
        # 3. Join rows with newline ('\n'.join(...))
        return '\n'.join([' '.join(map(str, row)) for row in self.data])

    def plus(self, other):
        """
        Performs Matrix Addition.
        Formula: Result[i][j] = A[i][j] + B[i][j]
        Returns: A NEW Matrix object (does not modify self).
        """
        # Initialize a new grid with zeros
        new_data = [[0] * self.size for _ in range(self.size)]
        
        for i in range(self.size):
            for j in range(self.size):
                # Add corresponding elements
                new_data[i][j] = self.data[i][j] + other.data[i][j]
        
        # Return result as an Object, not just a list
        return Matrix(new_data)

    def multiply(self, other):
        """
        Performs Matrix Multiplication.
        Formula: Result[i][j] = Sum(A[i][k] * B[k][j])
        Returns: A NEW Matrix object.
        """
        new_data = [[0] * self.size for _ in range(self.size)]
        
        # Triple Loop for Matrix Multiplication (O(N^3))
        for i in range(self.size):          # Row of Matrix A
            for j in range(self.size):      # Col of Matrix B
                for k in range(self.size):  # Common Index
                    # Dot Product calculation
                    new_data[i][j] += self.data[i][k] * other.data[k][j]
        
        return Matrix(new_data)

    def is_inverse_of(self, other):
        """
        Checks if 'other' is the Inverse Matrix of 'self'.
        Logic: A * B must equal the Identity Matrix (I).
        """
        # 1. Calculate the product
        product_matrix = self.multiply(other)
        
        # 2. Generate Identity Matrix (Diagonal is 1, rest are 0)
        # List Comprehension Logic: 1 if row==col else 0
        identity = [[1 if i == j else 0 for j in range(self.size)] for i in range(self.size)]
        
        # 3. Compare the raw data
        if product_matrix.data == identity:
            return True
        else:
            return False

# ---- Main Execution Logic ----

# Helper function to read N lines of input
def get_matrix_input(n):
    matrix = []
    for _ in range(n):
        # Map input string to integers and convert to list
        matrix.append(list(map(int, sys.stdin.readline().split())))
    return matrix

# Read Metadata (Size N and Command)
line = sys.stdin.readline().split()
if line:
    N = int(line[0])
    command = line[1]

    # Instantiate Objects
    # We pass the raw list from get_matrix_input into the Matrix Class Constructor
    matrix_A = Matrix(get_matrix_input(N))
    matrix_B = Matrix(get_matrix_input(N))

    # Execute Command
    if command == 'plus':
        result = matrix_A.plus(matrix_B)
        print("Sum of Matrices:")
        print(result) # Calls __str__ automatically

    elif command == 'multiply':
        result = matrix_A.multiply(matrix_B)
        print("Product of Matrices:")
        print(result)

    elif command == 'inverse_check':
        if matrix_A.is_inverse_of(matrix_B):
            print("The matrices are inverse to each other.")
        else:
            print("The matrices are NOT inverse.")