import sys
set.sysrecursionlimit(10**6)

N = int(sys.stdin.readline())
M = int(sys.stdin.readline())
parent = [i for i in range(N + 1)]

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

L = [[0] * (N + 1)]

for j in range(N):
    row = list(map(int, sys.stdin.readline().split()))
    row = [0] + row
    L.append(row)

for y in range(1, N + 1):
    for x in range(1, N + 1):
        if L[y][x] == 1:
            union(y, x)

target = list(map(int, sys.stdin.readline().split()))
standard = find(target[0])

for k in range(M):
    if find(target[k]) != standard:
        print("NO")
        sys.exit(0)

print("YES")