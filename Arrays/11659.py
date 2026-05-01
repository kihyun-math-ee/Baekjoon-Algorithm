import sys

N, M = map(int, sys.stdin.readline().split())
sequence = list(map(int, sys.stdin.readline().split()))
F = [0]
p_sum = 0

for num in sequence:
    p_sum += num
    F.append(p_sum)

for _ in range(M):
    i, j = map(int, sys.stdin.readline().split())
    print(F[j] - F[i-1])