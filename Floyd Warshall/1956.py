import sys

V, E = map(int, sys.stdin.readline().split())
graph = [[float('inf')] * (V + 1) for _ in range(V + 1)]
min_result = float('inf')

for _ in range(E):
    a, b, c = map(int, sys.stdin.readline().split())
    graph[a][b] = min(graph[a][b], c)

for k in range(1, V + 1):
    for i in range(1, V + 1):
        for j in range(1, V + 1):
            graph[i][j] = min(graph[i][j], graph[i][k] + graph[k][j])

for l in range(1, V + 1):
    if graph[l][l] < min_result:
        min_result = graph[l][l]

if min_result == float('inf'):
    print(-1)

else:
    print(min_result)
        