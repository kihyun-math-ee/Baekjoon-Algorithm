import sys
H, M = map(int, sys.stdin.readline().split())
total_min = H * 60 + M - 45

if total_min < 0:
    total_min += 24 * 60

print(total_min // 60, total_min % 60)

