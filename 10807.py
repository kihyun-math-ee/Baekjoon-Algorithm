import sys
N = int(sys.stdin.readline())
data = list(map(int, sys.stdin.readline().split()))
v = int(sys.stdin.readline())

cnt = 0
for x in data:
    if x == v:
        cnt += 1
print(cnt)
