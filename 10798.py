import sys

Matrix = []
for _ in range(5):
    line = sys.stdin.readline().strip()
    Matrix.append(line)

max_length = max(len(row) for row in Matrix)

for j in range(max_length):
    for i in range(5):
        if j < len(Matrix[i]):
            print(Matrix[i][j], end="")