import sys

T = int(sys.stdin.readline())
for _ in range(T):
    sequence = sorted(list(map(int, sys.stdin.readline().split())))
    print(sequence[-3])