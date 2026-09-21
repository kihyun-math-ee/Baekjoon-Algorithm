import sys
import math

n = int(sys.stdin.readline())
parent = [i for i in range(n + 1)]
target = []
stars = []
total_cost = 0

def find(x):
    if parent[x] != x:
        parent[x] = find(parent[x])
    return parent[x]

def union(a, b):
    root_a = parent[a]
    root_b = parent[b]

    if root_a != root_b:
        if root_a < root_b:
            parent[root_b] = root_a
        else:
            parent[root_a] = root_b

for _ in range(n):
    x, y = map(float, sys.stdin.readline().split())
    stars.append((x, y))

for i in range(0, n - 1):
    for j in range(i + 1, n):
        target.append(((math.sqrt((stars[i][0] - stars[j][0]) ** 2 + (stars[i][1] - stars[j][1]) ** 2)), i, j))

target.sort()

for edge in target:
    c, a, b = edge

    if find(a) != find(b):
        union(a, b)
        total_cost += c

print(f"{total_cost:.2f}")