import sys

N, M = map(int, sys.stdin.readline().split())
L = []

for _ in range(N):
    target = int(sys.stdin.readline())
    L.append(target)

L.sort()
min_diff = float('inf')
left = 0
right = 0

while left <= right and right <= N - 1:
    if L[right] - L[left] == M:
        print(M)
        sys.exit(0)
    elif L[right] - L[left] > M:
        if L[right] - L[left] < min_diff:
            min_diff = L[right] - L[left]
        left += 1
    elif L[right] - L[left] < M:
        right += 1

print(min_diff)