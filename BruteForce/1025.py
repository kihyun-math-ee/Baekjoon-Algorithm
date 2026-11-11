import sys
import math

L = []
max_square = -1
N, M = map(int, sys.stdin.readline().split())

for _ in range(N):
    row = sys.stdin.readline().strip()
    L.append(row)

for y in range(N):
    for x in range(M):
        for dy in range(-N, N):
            for dx in range(-M, M):
                if dy == 0 and dx == 0:
                    continue
                S = ""
                ny, nx = y, x
                while 0 <= ny < N and 0 <= nx < M:
                    S += L[ny][nx]
                    num = int(S)
                    if math.sqrt(num) == int(math.sqrt(num)):
                        if max_square < num:
                            max_square = num
                    ny += dy
                    nx += dx

print(max_square)