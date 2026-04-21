import sys

n = int(sys.stdin.readline())
L = list(map(int, sys.stdin.readline().split()))

total_sum = sum(L)
ans = 0

for num in L:
    total_sum -= num
    ans += num * total_sum

print(ans)