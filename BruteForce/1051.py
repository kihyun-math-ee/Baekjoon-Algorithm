import sys

N, M = map(int, sys.stdin.readline().split())
L = []
max_area = 0

for _ in range(N):
    row = sys.stdin.readline().strip()
    row_list = list(row)
    L.append(row_list)

for y in range(N):
    for x in range(M):
        for k in range(min(N - y, M - x)):
            if (L[y][x] == L[y][x+k]) and (L[y][x] == L[y+k][x]) and (L[y][x] == L[y+k][x+k]):
                if (k+1)**2 >= max_area:
                    max_area = (k+1)**2

print(max_area)