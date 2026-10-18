import sys

n = int(sys.stdin.readline())

if n == 0:
    print(0)
    sys.exit(0)

else:
    high = n
    low = 1
    mid = (high + low) // 2
    result = 0

    while low <= high:
        mid = (high + low) // 2

        if (mid ** 2) >= n:
            high = mid - 1
            result = mid

        else:
            low = mid + 1

    print(result)