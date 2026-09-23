import sys

N = int(sys.stdin.readline())
min_X = 10001
min_Y = 10001
max_X = -10001
max_Y = -10001
target = []

for _ in range(N):
    X, Y = map(int, sys.stdin.readline().split())
    target.append((X, Y))
    if X <= min_X:
        min_X = X
    if X >= max_X:
        max_X = X
    if Y <= min_Y:
        min_Y = Y
    if Y >= max_Y:
        max_Y = Y

L = max(max_X - min_X, max_Y - min_Y)

def is_on_boundary(sx, sy, length):
    for x, y in target:
        on_vertical = (x == sx or x == sx + length) and (sy <= y <= sy + length)
        on_horizontal = (y == sy or y == sy + length) and (sx <= x <= sx + length)

        if not (on_vertical or on_horizontal):
            return False
    return True

cand1_sx, cand1_sy = min_X, min_Y
cand2_sx, cand2_sy = max_X - L, max_Y - L

if is_on_boundary(cand1_sx, cand1_sy, L) or is_on_boundary(cand2_sx, cand2_sy, L):
    print(L)
else:
    print(-1)

