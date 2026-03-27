import sys

def punch_hole(size, r, c):
    global initial
    if size == 1:
        return

    for i in range(r + (size // 3), r + (size // 3) * 2):
        for j in range(c + (size // 3), c + (size // 3) * 2):
            initial[i][j] = ' '
    punch_hole(size // 3, r, c)
    punch_hole(size // 3, r, c + (size // 3))
    punch_hole(size // 3, r, c + (size // 3) * 2)
    punch_hole(size // 3, r + (size // 3), c)
    punch_hole(size // 3, r + (size // 3), c + (size // 3) * 2)
    punch_hole(size // 3, r + (size // 3) * 2, c)
    punch_hole(size // 3, r + (size // 3) * 2, c + (size // 3))
    punch_hole(size // 3, r + (size // 3) * 2, c + (size // 3) * 2)

N = int(sys.stdin.readline())
initial = [['*'] * N for _ in range(N)]
punch_hole(N, 0, 0)
for k in range(N):
    print(''.join(initial[k]))

        
        
