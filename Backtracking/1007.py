import sys
import math
sys.setrecursionlimit(10 ** 6)

T = int(sys.stdin.readline())

def backtracking(depth, current_a, current_b, start):
    global min_length

    if depth == N // 2:
        x_result = x_sum - (2 * current_a)
        y_result = y_sum - (2 * current_b)
        min_length = min(min_length, (x_result ** 2) + (y_result ** 2))
        return

    for k in range(start, N):
        backtracking(depth + 1, current_a + vector[k][0], current_b + vector[k][1], k + 1)


for _ in range(T):
    N = int(sys.stdin.readline())
    vector = []
    L = []
    min_length = float('inf')
    x_sum = 0
    y_sum = 0

    for _ in range(N):
        x, y = map(int, sys.stdin.readline().split())
        vector.append((x, y))
        x_sum += x
        y_sum += y
    
    backtracking(1, vector[0][0], vector[0][1], 1)
    print(math.sqrt(min_length))
    