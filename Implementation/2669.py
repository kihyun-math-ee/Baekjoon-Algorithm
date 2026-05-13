import sys

L = [[0] * 101 for _ in range(101)]

for j in range(4):
    X_1, Y_1, X_2, Y_2 = map(int, sys.stdin.readline().split())
    for n in range(Y_1, Y_2):
        for m in range(X_1, X_2):
            L[n][m] = 1

result = 0

for k in range(0, 101):
    result += sum(L[k])

print(result)
