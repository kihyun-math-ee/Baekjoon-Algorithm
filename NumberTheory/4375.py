import sys

while True:
    line = sys.stdin.readline()

    if not line:
        break

    n = int(line)
    target = 1
    l = 1
    while True:
        if target % n == 0:
            print(l)
            break

        target = (target * 10) + 1
        target = target % n
        l += 1