import sys

N, b = map(int, sys.stdin.readline().split())

S = (1 << (b + 1)) - 1

if S >= N:
    print('yes')

else:
    print('no')