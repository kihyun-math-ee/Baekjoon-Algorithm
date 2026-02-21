import sys
x, y, w, h = map(int, sys.stdin.readline().split())
L_1 = abs(w - x)
L_2 = abs(x)
L_3 = abs(h - y)
L_4 = abs(y)
L = [L_1, L_2, L_3, L_4]
print(min(L))