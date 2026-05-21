import sys

target = sys.stdin.readline().strip()
N = int(sys.stdin.readline())
cnt = 0

for _ in range(N):
    S = sys.stdin.readline().strip()
    S = S + S
    if target in S:
        cnt += 1

print(cnt)