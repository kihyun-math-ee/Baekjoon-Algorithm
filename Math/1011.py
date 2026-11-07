import sys
import math

T = int(sys.stdin.readline())

for _ in range(T):
    x, y = map(int, sys.stdin.readline().split())
    distance = y - x
    cnt = 0
    k = 1
    end = False

    while True:
        if distance - (2 * k) == 0:
            cnt += 2
            end = True
            break
        elif distance - (2 * k) < 0:
            break
        else:
            distance -= (2 * k)
            k += 1
            cnt += 2

    if end:
        print(cnt)
    else:
        residue = math.ceil(distance / k)
        print(cnt + residue)