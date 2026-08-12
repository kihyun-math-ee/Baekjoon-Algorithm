import sys

K, N = map(int, sys.stdin.readline().split())
L = []

for _ in range(K):
    line = int(sys.stdin.readline())
    L.append(line)

L.sort()
high = max(L)
low = 1
mid = (high + low) // 2
result = 0

while low <= high:
    S = 0
    mid = (high + low) // 2

    for i in range(K):
        S += L[i] // mid

    if S >= N:
        result = mid
        low = mid + 1

    else:
        high = mid - 1

print(result)