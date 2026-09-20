import sys

sys.setrecursionlimit(10**6)
n, m = map(int, sys.stdin.readline().split())
parent = [i for i in range(n + 1)]

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

for _ in range(m):
    x, a, b = map(int, sys.stdin.readline().split())

    if x == 0:
        union(a, b)

    else:
        if find(a) == find(b):
            print("YES")
        else:
            print("NO")