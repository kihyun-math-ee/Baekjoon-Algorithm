import sys

N = int(sys.stdin.readline())
scores = list(map(int, sys.stdin.readline().split()))

print(sum(scores) * 100 / max(scores) / N)