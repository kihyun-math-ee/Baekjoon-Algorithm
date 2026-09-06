import sys

N, M = map(int, sys.stdin.readline().split())
L = list(map(int, sys.stdin.readline().split()))

high = sum(L)
low = max(L)
result = float('inf')

while low <= high:
    mid = (high + low) // 2
    num = 1
    s = 0

    for i in range(N):

        if s + L[i] <= mid:
            s += L[i]

        elif s + L[i] > mid:
            num += 1
            s = L[i]

        if num > M:
            low = mid + 1
            break

    if num <= M:
        high = mid - 1
        if result > mid:
            result = mid

print(result)