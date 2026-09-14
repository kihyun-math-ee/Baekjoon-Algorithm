import sys

n, m, r = map(int, sys.stdin.readline().split())
L = list(map(int, sys.stdin.readline().split()))
L = [0] + L
graph = [[float('inf')] * (n + 1) for _ in range(n + 1)]
max_item = 0

for _ in range(r):
    a, b, l = map(int, sys.stdin.readline().split())
    graph[a][b] = min(graph[a][b], l)
    graph[b][a] = min(graph[b][a], l)

for k in range(1, n + 1):
    for i in range(1, n + 1):
        for j in range(1, n + 1):
            if i != j:
                graph[i][j] = min(graph[i][j], graph[i][k] + graph[k][j])

for y in range(1, n + 1):
    item_sum = L[y]
    for x in range(1, n + 1):
        if graph[y][x] <= m:
            item_sum += L[x]
    if item_sum > max_item:
        max_item = item_sum

print(max_item)