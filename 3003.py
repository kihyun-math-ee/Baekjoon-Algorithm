import sys

ORIGIN = [1, 1, 2, 2, 2, 8]
found = list(map(int, sys.stdin.readline().split()))

result = []
for o, f in zip(ORIGIN, found):
    result.append(o - f)

print(*result)