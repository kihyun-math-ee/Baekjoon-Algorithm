import sys

N = int(sys.stdin.readline())
sequence = list(map(int, sys.stdin.readline().split()))
sequence = [0] + sequence
prefix_sum = [0] * (N + 1)
prime_num = [True] * 10000001
prime_num[0] = False
prime_num[1] = False
cnt = 0

for j in range(2, 1000001):
    if prime_num[j]:
        for k in range(j * 2, 1000001, j):
                prime_num[k] = False

for i in range(1, N + 1):
    prefix_sum[i] = prefix_sum[i - 1] + sequence[i]

for y in range(1, N):
    for x in range(2, N + 2 - y):
        if prime_num[x] == True:
            if prime_num[prefix_sum[y + x - 1] - prefix_sum[y - 1]] == True:
                cnt += 1

print(cnt)        