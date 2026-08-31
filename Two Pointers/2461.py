import sys

N, M = map(int, sys.stdin.readline().split())
L = []

if N == 1:
    print(0)
    sys.exit(0)

L = []

for i in range(N):
    row = list(map(int, sys.stdin.readline().split()))
    for j in range(M):
        L.append((row[j], i))

L.sort()
left = 0
right = 0
min_max_diff = float('inf')
classes_cnt = [0] * N
current_classes = 0

while left < N * M:
    if current_classes < N and right < N * M:
        if classes_cnt[L[right][1]] == 0:
            current_classes += 1
        classes_cnt[L[right][1]] += 1
        right += 1

    elif current_classes == N:
        if L[right - 1][0] - L[left][0] < min_max_diff:
            min_max_diff = L[right - 1][0] - L[left][0]

        classes_cnt[L[left][1]] -= 1
        if classes_cnt[L[left][1]] == 0:
            current_classes -= 1
        left += 1

    else:
        break
    
print(min_max_diff)