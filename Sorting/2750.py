import sys

num_list = []
N = int(sys.stdin.readline())

for _ in range(N):
    num = int(sys.stdin.readline())
    num_list.append(num)
sorted_num_list = sorted(num_list)

for i in range(N):
    print(sorted_num_list[i])