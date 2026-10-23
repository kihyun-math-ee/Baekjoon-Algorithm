import sys
sys.setrecursionlimit(10 ** 6)

N, M = map(int, sys.stdin.readline().split())
T = list(map(int, sys.stdin.readline().split()))
parent = [i for i in range(N + 1)]
parties = []
cnt = 0

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

if T[0] == 0:
    print(M)

else:
    for k in range(1, T[0]):
        union(T[k], T[k + 1])
    for _ in range(M):
        L = list(map(int, sys.stdin.readline().split()))
        n = L[0]
        target = L[1:]
        parties.append(target)
        for j in range(len(target) - 1):
            union(target[j], target[j + 1])

    truth_anchor = find(T[1])

    for p in parties:
        if find(p[0]) != truth_anchor:
            cnt += 1

    print(cnt)