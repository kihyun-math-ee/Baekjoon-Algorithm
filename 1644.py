import sys
import math

N = int(sys.stdin.readline())

if N <= 1:
    print(0)
    sys.exit(0)

max_size = N + 1
is_prime = [True] * max_size
is_prime[0] = False
is_prime[1] = False
m = int(math.sqrt(max_size))
primes = []

for i in range(2, m + 1):
    if is_prime[i]:
        for j in range(i * 2, max_size, i):
            is_prime[j] = False

for k in range(2, max_size):
    if is_prime[k]:
        primes.append(k)

left, right = 0, 0
current_sum = 0
cnt = 0

while True:
    if current_sum >= N:
        if current_sum == N:
            cnt += 1
        current_sum -= primes[left]
        left += 1

    elif right == len(primes):
        break

    else:
        current_sum += primes[right]
        right += 1

print(cnt)