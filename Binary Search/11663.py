import sys

N, M = map(int, sys.stdin.readline().split())
L = list(map(int, sys.stdin.readline().split()))
L.sort()

def upper_bound(arr, target):
    high = len(arr)
    low = 0

    while low < high:
        mid = (high + low) // 2

        if arr[mid] > target:
            high = mid

        else:
            low = mid + 1

    return low

def lower_bound(arr, target):
    high = len(arr)
    low = 0

    while low < high:
        mid = (high + low) // 2

        if arr[mid] >= target:
            high = mid

        else:
            low = mid + 1

    return low

for _ in range(M):
    A, B = map(int, sys.stdin.readline().split())
    print(upper_bound(L, B) - lower_bound(L, A))