import sys

N, L = map(int, sys.stdin.readline().split())
integer_list = list(map(int, sys.stdin.readline().split()))
integer_list.sort()

for i in range(N):
    if integer_list[i] <= L:
        L += 1

print(L)
