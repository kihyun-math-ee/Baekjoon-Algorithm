import sys

n = int(sys.stdin.readline())
x_dict = {}
y_dict = {}
cnt = 0

for i in range(n):
    x, y = map(int, sys.stdin.readline().split())
    if x in x_dict:
        x_dict[x] += 1
    else:
        x_dict[x] = 1 
    if y in y_dict:
        y_dict[y] += 1
    else:
        y_dict[y] = 1
    
for count in x_dict.values():
    if count >= 2:
        cnt += 1

for count in y_dict.values():
    if count >= 2:
        cnt += 1

print(cnt)
    