import sys

N = int(sys.stdin.readline())
L_X = []
L_Y = []

for _ in range(N):
    X, Y = map(int, sys.stdin.readline().split())
    L_X.append(X)
    L_Y.append(Y)

width = max(L_X) - min(L_X)
height = max(L_Y) - min(L_Y)
print(width * height)
