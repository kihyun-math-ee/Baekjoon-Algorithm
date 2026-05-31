import sys

a, b = map(int, sys.stdin.readline().split())
N = int(sys.stdin.readline())
x_list = [0, a]
y_list = [0, b]
max_x = 0
max_y = 0

for _ in range(N):
    m, n = map(int, sys.stdin.readline().split())
    if m == 1:
        x_list.append(n)
    else:
        y_list.append(n)

x_list.sort(reverse=True)
y_list.sort(reverse=True)

for i in range(len(x_list)-1):
    if x_list[i] - x_list[i+1] > max_x:
        max_x = x_list[i] - x_list[i+1] 

for j in range(len(y_list)-1):
    if y_list[j] - y_list[j+1] > max_y:
        max_y = y_list[j] - y_list[j+1]

M = max_x * max_y
print(M)