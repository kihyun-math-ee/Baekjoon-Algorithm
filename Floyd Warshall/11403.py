import sys

N = int(sys.stdin.readline())
graph = [[0] * (N + 1) for _ in range(N + 1)]

for y in range(1, N + 1):
    row = list(map(int, sys.stdin.readline().split()))
    row = [0] + row
    for x in range(1, N + 1):
        graph[y][x] = row[x]

for k in range(1, N + 1):
    for i in range(1, N + 1):
        for j in range(1, N + 1):
            if graph[i][k] == 1 and graph[k][j] == 1:
                graph[i][j] = 1

for r in range(1, N + 1):
    print(*graph[r][1:])