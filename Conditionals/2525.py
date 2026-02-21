import sys

A, B = map(int, sys.stdin.readline().split())
C = int(sys.stdin.readline())
total_min = A * 60 + B + C

print((total_min // 60) % 24, total_min % 60)

