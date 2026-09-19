import sys
sys.setrecursionlimit(10**6)
T = int(sys.stdin.readline())

def find(x):
    if friends[x] != x:
        friends[x] = find(friends[x])

    return friends[x]

def union(a, b):
    root_a = find(a)
    root_b = find(b)

    if root_a == root_b:
        return sizes[root_a]

    elif root_a != root_b:
        if root_a < root_b:
            sizes[root_b] += sizes[root_a]
            friends[root_a] = root_b
            return sizes[root_b]
        else:
            sizes[root_a] += sizes[root_b]
            friends[root_b] = root_a
            return sizes[root_a]

for _ in range(T):
    friends = {}
    sizes = {}
    F = int(sys.stdin.readline())

    for _ in range(F):
        A, B = sys.stdin.readline().split()

        if A not in friends:
            friends[A] = A
            sizes[A] = 1

        if B not in friends:
            friends[B] = B
            sizes[B] = 1

        print(union(A, B))