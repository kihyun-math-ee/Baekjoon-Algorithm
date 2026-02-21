import sys

x_1, y_1 = map(int, sys.stdin.readline().split())
x_2, y_2 = map(int, sys.stdin.readline().split())
x_3, y_3 = map(int, sys.stdin.readline().split())

if x_1 == x_2:
    ans_x = x_3
elif x_1 == x_3:
    ans_x = x_2
else:
    ans_x = x_1

if y_1 == y_2:
    ans_y = y_3
elif y_1 == y_3:
    ans_y = y_2
else:
    ans_y = y_1

print(ans_x, ans_y)
