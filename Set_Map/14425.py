import sys

N, M = map(int, sys.stdin.readline().split())
my_set = set()
target_cnt = 0

for _ in range(N):
    my_strings = sys.stdin.readline().strip()
    my_set.add(my_strings)

for _ in range(M):
    target_strings = sys.stdin.readline().strip()
    if target_strings in my_set:
        target_cnt += 1

print(target_cnt)