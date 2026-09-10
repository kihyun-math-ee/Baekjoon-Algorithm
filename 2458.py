import sys

N, M = map(int, sys.stdin.readline().split())
adjacent = [[float('inf')] * (N + 1) for _ in range(N + 1)]
result = 0

for u in range(1, N + 1):
    for v in range(1, N + 1):
        if u == v:
            adjacent[u][v] = 0

for _ in range(M):
    a, b = map(int, sys.stdin.readline().split())
    adjacent[a][b] = 1

for k in range(1, N + 1):
    for i in range(1, N + 1):
            for j in range(1, N + 1):
                adjacent[i][j] = min(adjacent[i][j], adjacent[i][k] + adjacent[k][j])

for r in range(1, N + 1):
    cnt = 0
    for c in range(1, N + 1):
        if r != c:
            if adjacent[r][c] != float('inf') or adjacent[c][r] != float('inf'):
                cnt += 1
    if cnt == N - 1:
        result += 1

print(result)