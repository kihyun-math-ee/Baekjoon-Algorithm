import sys

dp = [0] * 100001
dp[1] = 1

for i in range(2, 100001):
    dp[i] = dp[i - 1] + dp[i - 2]

T = int(sys.stdin.readline())

for _ in range(T):
    target = int(sys.stdin.readline())
    high = 100000
    low = 0
    is_printed = False

    while low <= high:
        mid = (high + low) // 2

        if dp[mid] == target:
            print(mid)
            is_printed = True
            break

        elif dp[mid] < target:
            low = mid + 1

        elif dp[mid] > target:
            high = mid - 1

    if not is_printed:
        print(mid)