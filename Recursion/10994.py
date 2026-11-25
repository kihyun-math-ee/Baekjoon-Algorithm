import sys

def punch_hole(size, r, c):
    global initial
    if size == 1:
        return

    length = 4 * size - 3

    for i in range(c + 1, c + length - 1):
        initial[r + 1][i] = ' '
        initial[r + length - 2][i] = ' '

    for i in range(r + 1, r + length - 1):
        initial[i][c + 1] = ' '
        initial[i][c + length - 2] = ' '

    punch_hole(size - 1, r + 2, c + 2)

N = int(sys.stdin.readline())
length = 4 * N - 3
initial = [['*'] * length for _ in range(length)]
punch_hole(N, 0, 0)

for k in range(length):
    print(''.join(initial[k]))
