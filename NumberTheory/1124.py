import sys

A, B = map(int, sys.stdin.readline().split())
underprime = 0

for i in range(A, B + 1):
    num = i
    cnt = 0
    j = 2

    while j * j <= num:
        while num % j == 0:
            num //= j
            cnt += 1
        j += 1

    if num > 1:
        cnt += 1

    if cnt < 2:
        continue

    is_prime = True
    k = 2

    while k * k <= cnt:
        if cnt % k == 0:
            is_prime = False
            break
        k += 1

    if is_prime:
        underprime += 1

print(underprime)
