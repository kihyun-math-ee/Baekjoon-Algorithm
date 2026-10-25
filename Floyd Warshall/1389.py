import sys

N, M = map(int, sys.stdin.readline().split())
adjacency = [[float('inf')] * (N + 1) for _ in range(N + 1)]
min_sum = float('inf')
num = 0

for a in range(1, N + 1):
    for b in range(1, N + 1):
        if a == b:
            adjacency[a][b] = 0

for _ in range(M):
    A, B = map(int, sys.stdin.readline().split())
    adjacency[A][B] = 1
    adjacency[B][A] = 1

for k in range(1, N + 1):
    for i in range(1, N + 1):
        for j in range(1, N + 1):
            adjacency[i][j] = min(adjacency[i][j], adjacency[i][k] + adjacency[k][j])

for r in range(1, N + 1):
    if sum(adjacency[r][1:]) < min_sum:
        min_sum = sum(adjacency[r][1:])
        num = r

print(num)