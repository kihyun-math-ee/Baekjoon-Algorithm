import sys

S = int(sys.stdin.readline())
n = 1
target = 0

while True:
    if target < S:
        target += n
        n += 1
    elif target == S:
        print(n-1)
        break
    else:
        print(n-2)
        break
        