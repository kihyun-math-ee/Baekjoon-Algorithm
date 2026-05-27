import sys

N = int(sys.stdin.readline())
L = []
    
for _ in range(N):
    line = list(map(int, sys.stdin.readline().split()))
    L.append(line)

friends = [set() for _ in range(N)]

for x in range(5):
    for y in range(N-1):
        for y_compare in range(y+1, N):
            if L[y][x] == L[y_compare][x]:
                friends[y].add(y_compare)
                friends[y_compare].add(y)

M = -1
president = 0

for i in range(N):
    if len(friends[i]) > M:
        M = len(friends[i])
        president = i + 1

print(president)