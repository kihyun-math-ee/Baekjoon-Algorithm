import sys
from collections import deque

L = []
M, N = map(int, sys.stdin.readline().split())
L.append([-1] * (M + 2))
target = deque()
zero_cnt = 0

for _ in range(N):
    row = list(map(int, sys.stdin.readline().split()))
    row = [-1] + row + [-1]
    L.append(row)

L.append([-1] * (M + 2))

for y in range(1, N + 1):
    for x in range(1, M + 1):
        if L[y][x] == 1:
            target.append((y, x, 0))
        elif L[y][x] == 0:
            zero_cnt += 1

is_possible = False

if zero_cnt == 0:
    is_possible = True
    print(0)

else:
    while target:
        if zero_cnt == 0:
            for _ in range(len(target)):
                current = target.popleft()
            is_possible = True
            print(current[2])
            break
        
        else:
            current = target.popleft()
            if L[current[0] + 1][current[1]] == 0:
                L[current[0] + 1][current[1]] = 1
                zero_cnt -= 1
                target.append((current[0] + 1, current[1], current[2] + 1))
                
            if L[current[0]][current[1] + 1] == 0:
                L[current[0]][current[1] + 1] = 1
                zero_cnt -= 1
                target.append((current[0], current[1] + 1, current[2] + 1))

            if L[current[0] - 1][current[1]]== 0:
                L[current[0] - 1][current[1]] = 1
                zero_cnt -= 1
                target.append((current[0] - 1, current[1], current[2] + 1))

            if L[current[0]][current[1] - 1] == 0:
                L[current[0]][current[1] - 1] = 1
                zero_cnt -= 1
                target.append((current[0], current[1] - 1, current[2] + 1))

if is_possible == False:
    print(-1)