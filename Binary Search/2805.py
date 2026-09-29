import sys

N, M = map(int, sys.stdin.readline().split())
tree = list(map(int, sys.stdin.readline().split()))
tree.sort()
high = max(tree)
low = 0
mid = (high + low) // 2
target = 0

while low <= high:
    S = 0
    mid = (high + low) // 2

    for i in range(N):
        if tree[i] > mid:
            S += tree[i] - mid

    if S >= M:
        target = mid

        low = mid + 1

    elif S < M:
        high = mid - 1

print(target)