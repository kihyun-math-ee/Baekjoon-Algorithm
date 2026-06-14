import sys

N = int(sys.stdin.readline())
target = list(map(int, sys.stdin.readline().split()))
F = target.copy()
F.sort()
F.reverse()

if target == F:
    print(-1)
    sys.exit(0)

else:
    for i in range(1, N + 1):
        for j in range(1, i):
            if target[-i] < target[-j]:
                target[-i], target[-j] = target[-j], target[-i]
                target[N-i+1:] = sorted(target[N-i+1:])
                print(*target)
                sys.exit(0)
