import sys

check = [0] * 31

for _ in range(28):
    n = int(sys.stdin.readline())
    check[n] = 1

for i in range(1, 31):
    if check[i] == 0:
        print(i)