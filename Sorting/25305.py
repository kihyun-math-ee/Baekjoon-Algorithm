import sys

N, k = map(int, sys.stdin.readline().split())
x = list(map(int, sys.stdin.readline().split()))
sort_x = sorted(x)
print(sort_x[-k])