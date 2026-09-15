import sys
sys.setrecursionlimit(10**6)

n, m = map(int, sys.stdin.readline().split())
parent = [i for i in range(n)]

def find(x):
    if parent[x] != x:
        parent[x] = find(parent[x])

    return parent[x]

def union(a, b):
    root_a = find(a)
    root_b = find(b)

    if root_a == root_b:
        return True
    if root_a != root_b:
        if root_a < root_b:
            parent[root_b] = root_a
            return False
        else:
            parent[root_a] = root_b
            return False

for i in range(1, m + 1):
    A, B = map(int, sys.stdin.readline().split())
    if union(A, B) == True:
        print(i)
        sys.exit(0)

print(0)