import sys

L = {}
blank = []

def is_possible(l, coordinate):
    y_1 = coordinate[0] // 3
    x_1 = coordinate[1] // 3

    for a in range(9):
        if a != coordinate[0] and l[coordinate] == l[(a, coordinate[1])]:
            return False
        
    for b in range(9):
        if b != coordinate[1] and l[coordinate] == l[(coordinate[0], b)]:
            return False
        
    for m in range(y_1 * 3, y_1 * 3 + 3):
        for n in range(x_1 * 3, x_1 * 3 + 3):
            if (m, n) != coordinate and l[coordinate] == l[(m, n)]:
                return False
            
    return True

def sudoku(start, l, b):
    if start == len(b):
        for y in range(9):
            for x in range(9):
                print(l[(y, x)], end=' ')
            print()
        sys.exit(0)

    current_blank = b[start]

    for j in range(1, 10):
        l[current_blank] = j
        if is_possible(l, current_blank):
            sudoku(start + 1, l, b)

        l[current_blank] = 0

for y in range(9):
    line = list(map(int, sys.stdin.readline().split()))
    for x in range(9):
        L[(y, x)] = line[x]
        if line[x] == 0:
            blank.append((y, x))

sudoku(0, L, blank)
