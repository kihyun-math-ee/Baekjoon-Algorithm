import sys

def spiral(n, r, c):
    global L
    if n == 1:
        for i in range(r, r + 3):
            L[i][c] = '*'
        return

    row_num = 4 * n - 1
    col_num = 4 * n - 3

    for i in range(c, c + col_num):
        L[r][i] = '*'
        L[r + row_num - 1][i] = '*'

    for i in range(r, r + row_num):
        L[i][c] = '*'

    for i in range(r + 2, r + row_num):
        L[i][c + col_num - 1] = '*'

    L[r + 2][c + col_num - 2] = '*'
    spiral(n - 1, r + 2, c + 2)

N = int(sys.stdin.readline())

if N == 1:
    print('*')
else:
    row_num = 4 * N - 1
    col_num = 4 * N - 3
    L = [[' '] * col_num for _ in range(row_num)]
    spiral(N, 0, 0)

    for i in range(row_num):
        print(''.join(L[i]).rstrip())
