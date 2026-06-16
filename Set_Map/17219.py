import sys

N, M = map(int, sys.stdin.readline().split())
example = {}

for _ in range(N):
    site, password = sys.stdin.readline().split()
    example[site] = password

for _ in range(M):
    target = sys.stdin.readline().strip()
    print(example[target])
    
