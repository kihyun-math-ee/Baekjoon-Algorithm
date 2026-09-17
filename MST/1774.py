import sys
import math

N, M = map(int, sys.stdin.readline().split())
parent = [i for i in range(N + 1)]
edges = []
vertex = [(0, 0)]
total_cost = 0

def find(x):
    if parent[x] != x:
        parent[x] = find(parent[x])

    return parent[x]

def union(a, b):
    root_a = find(a)
    root_b = find(b)

    if root_a != root_b:
        if root_a < root_b:
            parent[root_b] = root_a
        else:
            parent[root_a] = root_b

for i in range(1, N + 1):
    X, Y = map(int, sys.stdin.readline().split())
    vertex.append((X, Y))
    
for j in range(1, N):
    for k in range(j + 1, N + 1):
        distance = math.sqrt((vertex[j][0] - vertex[k][0]) ** 2 + (vertex[j][1] - vertex[k][1]) ** 2)
        edges.append((distance, j, k))

edges.sort()

for _ in range(M):
    X, Y = map(int, sys.stdin.readline().split())
    union(X, Y)

for edge in edges:
    c, a, b = edge

    if find(a) != find(b):
        union(a, b)
        total_cost += c

print(f"{total_cost:.2f}")