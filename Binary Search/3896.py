import sys
import math

max_size = 1299710
L = [True] * max_size
L[0] = False
L[1] = False
s = int(math.sqrt(max_size))

for i in range(2, s + 1):
    if L[i] == True:
        for j in range(i * 2, max_size, i):
            L[j] = False

primes = []

for element in range(2, max_size):
    if L[element]:
        primes.append(element)

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

T = int(sys.stdin.readline())

for _ in range(T):
    k = int(sys.stdin.readline())

    if L[k] == True:
        print(0)

    else:
        idx = upper_bound(primes, k)       
        print(primes[idx] - primes[idx - 1])