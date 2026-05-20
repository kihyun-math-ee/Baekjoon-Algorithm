import sys

S = 0
N, b = map(int, sys.stdin.readline().split())

for i in range(0, b + 1):
    S += 2 ** i

if S >= N:
    print('yes')

else:
    print('no')