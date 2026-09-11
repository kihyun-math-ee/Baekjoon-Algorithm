import sys

n = int(sys.stdin.readline())
m = int(sys.stdin.readline())
graph = [[float('inf')] * (n + 1) for _ in range(n + 1)]
nxt = [[0] * (n + 1) for _ in range(n + 1)]

for y in range(1, n + 1):
    for x in range(1, n + 1):
        if y == x:
            graph[y][x] = 0
            

for _ in range(m):
    a, b, c = map(int, sys.stdin.readline().split())
    if c < graph[a][b]:
        graph[a][b] = c
        nxt[a][b] = b
     
for k in range(1, n + 1):
    for i in range(1, n + 1):
        for j in range(1, n + 1):
            if i != j:
                if graph[i][k] + graph[k][j] < graph[i][j]:
                    graph[i][j] = graph[i][k] + graph[k][j]
                    nxt[i][j] = nxt[i][k]

for row in range(1, n + 1):
    for column in range(1, n + 1):
        if graph[row][column] == float('inf'):
            graph[row][column] = 0

for z in range(1, n + 1):
    print(*graph[z][1:])

for i in range(1, n + 1):
    for j in range(1, n + 1):
        if nxt[i][j] == 0:
            print(0)
        else:
            path = []
            current = i
            path.append(current)
            while current != j:
                current = nxt[current][j]
                path.append(current)     
            print(len(path), *path)