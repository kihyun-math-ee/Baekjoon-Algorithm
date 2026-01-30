import sys

N = int(sys.stdin.readline())

# 1부터 N까지 순회 (변수 k 불필요)
for i in range(1, N + 1):
    print("*" * i)
