import sys

N = int(sys.stdin.readline())
L = []
cnt = 0

def is_promising(current_row):
    for previous_row in range(current_row):
        if L[current_row] == L[previous_row]:
            return False
        elif abs(current_row - previous_row) == abs(L[current_row] - L[previous_row]):
            return False
    
    return True

def N_Queen(row):
    global cnt

    if row == N:
        cnt += 1
        return

    for col in range(N):
        L.append(col)

        if is_promising(row):
            N_Queen(row + 1)

        L.pop()
    
N_Queen(0)
print(cnt)