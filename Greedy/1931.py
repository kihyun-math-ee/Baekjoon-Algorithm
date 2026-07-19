import sys

N = int(sys.stdin.readline())
target = []


for _ in range(N):
    a, b = map(int, sys.stdin.readline().split())
    target.append((a, b))

target.sort(key=lambda x: (x[1], x[0]))
cnt = 1
last_end_time = target[0][1]

for i in range(1, N):
    if last_end_time <= target[i][0]:
        cnt += 1
        last_end_time = target[i][1]

print(cnt)