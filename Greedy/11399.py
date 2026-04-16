import sys

N = int(sys.stdin.readline())
total = 0
current_sum = 0
people_list = list(map(int, sys.stdin.readline().split()))
people_list.sort()

for time in people_list:
    current_sum += time
    total += current_sum

print(total)