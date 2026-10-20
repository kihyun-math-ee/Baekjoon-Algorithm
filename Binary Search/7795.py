import sys

def lower_bound(arr, x):
    high = len(arr)
    low = 0

    while low < high:
        mid = (high + low) // 2

        if arr[mid] >= x:
            high = mid

        else:
            low = mid + 1

    return low

T = int(sys.stdin.readline())

for _ in range(T):
    N, M = map(int, sys.stdin.readline().split())
    target = list(map(int, sys.stdin.readline().split()))
    L = list(map(int, sys.stdin.readline().split()))
    L.sort()
    result = 0

    for i in range(N):
        result += (lower_bound(L, target[i]))

    print(result)