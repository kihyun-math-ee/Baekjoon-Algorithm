import sys

num_list = []

for _ in range(9):
    N = int(sys.stdin.readline())
    num_list.append(N)

max_val = max(num_list)

print(max_val)
print(num_list.index(max_val) + 1)

