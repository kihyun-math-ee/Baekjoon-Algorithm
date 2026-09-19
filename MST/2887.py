import sys

N = int(sys.stdin.readline())

if N == 1:
    print(0)
    sys.exit(0)

parent = [i for i in range(N + 1)]
x_list = []
y_list = []
z_list = []
edges = []
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
    x, y, z = map(int, sys.stdin.readline().split())
    x_list.append((x, i))
    y_list.append((y, i))
    z_list.append((z, i))

x_list.sort()
y_list.sort()
z_list.sort()

for j in range(N - 1):
    edges.append((x_list[j + 1][0] - x_list[j][0], x_list[j][1], x_list[j + 1][1]))
    edges.append((y_list[j + 1][0] - y_list[j][0], y_list[j][1], y_list[j + 1][1]))
    edges.append((z_list[j + 1][0] - z_list[j][0], z_list[j][1], z_list[j + 1][1]))

edges.sort()

for edge in edges:
    c, idx_1, idx_2 = edge
    if find(idx_1) != find(idx_2):
        union(idx_1, idx_2)
        total_cost += c

print(total_cost)