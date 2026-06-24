import sys

X, Y, W, S = map(int, sys.stdin.readline().split())
diagonal = min(X, Y)
parallel = diagonal * S + (max(X, Y) - diagonal) * W
combinational = (X + Y) * W

if (X + Y) % 2 == 0:
    zigzag = max(X, Y) * S

else:
    zigzag = (max(X, Y) - 1) * S + W

print(min(parallel, combinational, zigzag))    