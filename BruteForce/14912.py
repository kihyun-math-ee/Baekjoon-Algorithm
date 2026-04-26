import sys

n, d = map(int, sys.stdin.readline().split())
cnt = 0
for i in range(1, n + 1):
    cnt += str(i).count(str(d))

print(cnt)
