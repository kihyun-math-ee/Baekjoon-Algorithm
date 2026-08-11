import sys

N = int(sys.stdin.readline())
L = list(map(int, sys.stdin.readline().split()))
L.sort()
cnt = 0

for i in range(N):
    target = i
    left = 0
    right = N - 1

    while left < right:
        if left == i:
            left += 1
            continue
        if right == i:
            right -= 1
            continue
        if L[left] + L[right] == L[target]:
            cnt += 1
            break
        elif L[left] + L[right] > L[target]:
            right -= 1
        elif L[left] + L[right] < L[target]:
            left += 1

print(cnt)