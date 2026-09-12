import sys

n = int(sys.stdin.readline())
m = int(sys.stdin.readline())
graph = [[float('inf')] * (n + 1) for _ in range(n + 1)]

for x in range(1, n + 1):
    for y in range(1, n + 1):
        if x == y:
            graph[x][y] = 0

for _ in range(m):
    a, b, c = map(int, sys.stdin.readline().split())
    graph[a][b] = min(graph[a][b], c)

for k in range(1, n + 1):
    for i in range(1, n + 1):
        for j in range(1, n + 1):
            graph[i][j] = min(graph[i][j], graph[i][k] + graph[k][j])

for r in range(1, n + 1):
    for c in range(1, n + 1):
        if graph[r][c] == float('inf'):
            graph[r][c] = 0

for row in range(1, n + 1):
    print(*graph[row][1:])