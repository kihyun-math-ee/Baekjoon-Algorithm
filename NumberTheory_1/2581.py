import sys

M = int(sys.stdin.readline())
N = int(sys.stdin.readline())
S = []

for i in range(M, N + 1):
    if i == 1:
        continue
    is_prime = True

    for j in range(2, i):
        if i % j == 0:
            is_prime = False
            break
    if is_prime == True:
        S.append(i)

if len(S) == 0:
    print(-1)
else:
    print(sum(S))
    print(min(S))
