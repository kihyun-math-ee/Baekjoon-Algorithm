import sys

R, C, Q = map(int, sys.stdin.readline().split())
L = [[0] * (C + 1)]
prefix_sum = [[0] * (C + 1) for _ in range(R + 1)]

for i in range(R):
    row = list(map(int, sys.stdin.readline().split()))
    L.append([0] + row)

for y in range(1, R + 1):
    for x in range(1, C + 1):
        prefix_sum[y][x] = prefix_sum[y][x - 1] + prefix_sum[y - 1][x] - prefix_sum[y - 1][x - 1] + L[y][x]

for _ in range(Q):
    y1, x1, y2, x2 = map(int, sys.stdin.readline().split())
    d = (x2 - x1 + 1) * (y2 - y1 + 1)
    result = prefix_sum[y2][x2] - prefix_sum[y2][x1 - 1] - prefix_sum[y1 - 1][x2] + prefix_sum[y1 - 1][x1 - 1]
    print(result // d)