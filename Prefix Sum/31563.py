import sys

N, Q = map(int, sys.stdin.readline().split())
L = list(map(int, sys.stdin.readline().split()))
L = [0] + L
start = 0
prefix_sum = [0] * (N + 1)

for i in range(1, N + 1):
    prefix_sum[i] = prefix_sum[i - 1] + L[i]

for j in range(1, Q + 1):
    line = list(map(int, sys.stdin.readline().split()))
    
    if line[0] == 1:
        start = (start - line[1]) % N

    elif line[0] == 2:
        start = (start + line[1]) % N

    elif line[0] == 3:
        real_a = (start + line[1] - 1) % N
        real_b = (start + line[2] - 1) % N
        
        if real_a <= real_b:
            result = prefix_sum[real_b + 1] - prefix_sum[real_a]

        else:
            result = (prefix_sum[N] - prefix_sum[real_a]) + prefix_sum[real_b + 1]

        print(result)        