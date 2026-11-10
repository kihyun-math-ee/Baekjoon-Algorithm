import sys
import math

t = int(sys.stdin.readline())

def prime_result(x):
    if x <= 1:
        return False
    elif x == 2:
        return True
    else:
        return prime_check(x)

def prime_check(num):
    for i in range(2, int(math.sqrt(num)) + 1):
        if num % i == 0:
            return False
    return True

for _ in range(t):
    result = []
    target = list(map(int, sys.stdin.readline().split()))
    dp = [0] * (target[0] + 1)
    
    for j in range(1, target[0] + 1):
        dp[j] = dp[j - 1] + target[j]

    for length in range(2, target[0] + 1):
        for a in range(1, target[0] - length + 2):
            if prime_result(dp[a + length - 1] - dp[a - 1]):
                print(f"Shortest primed subsequence is length {length}: {' '.join(map(str, target[a:a + length]))}")
                result.append('success')
                break
        if result:
            break
    if not result:
        print('This sequence is anti-primed.')