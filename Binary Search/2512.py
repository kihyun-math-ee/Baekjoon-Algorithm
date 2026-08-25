import sys

N = int(sys.stdin.readline())
L = list(map(int, sys.stdin.readline().split()))
M = int(sys.stdin.readline())
max_cost = 0
L.sort()
high = max(L)
low = 1
mid = (high + low) // 2

while low <= high:
    total_cost = 0
    mid = (high + low) // 2

    for i in range(N):
        if mid >= L[i]:
            total_cost += L[i]
        else:
            total_cost += mid

    if total_cost > M:
        high = mid - 1

    else:
        low = mid + 1
        max_cost = mid

print(max_cost)