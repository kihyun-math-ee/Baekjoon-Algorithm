import sys
from collections import deque

M, N, H = map(int, sys.stdin.readline().split())
dz = [1, -1, 0, 0, 0, 0]
dy = [0, 0, 1, -1, 0, 0]
dx = [0, 0, 0, 0, 1, -1]
target = deque()
L = [[[-1] * (M + 2) for _ in range(N + 2)]]
is_visited = [[[False] * (M + 2) for _ in range(N + 2)] for _ in range(H + 2)]
minus_cnt = 0
visited_cnt = 0
day = 0

for _ in range(H):
    single_matrix = [[-1] * (M + 2)]
    for _ in range(N):
        line = list(map(int, sys.stdin.readline().split()))
        for num in line:
            if num == -1:
                minus_cnt += 1
        line = [-1] + line + [-1]
        single_matrix.append(line)
    single_matrix.append([-1] * (M + 2))
    L.append(single_matrix)

L.append([[-1] * (M + 2) for _ in range(N + 2)])

for z in range(1, H + 1):
    for y in range(1, N + 1):
        for x in range(1, M + 1):
            if L[z][y][x] == 1 and is_visited[z][y][x] == False:
                is_visited[z][y][x] = True
                visited_cnt += 1
                target.append((z, y, x, 0))
while target:
    current = target.popleft()
    if current[3] > day:
        day = current[3]
    for i in range(6):
        if L[current[0] + dz[i]][current[1] + dy[i]][current[2] + dx[i]] == 0 and is_visited[current[0] + dz[i]][current[1] + dy[i]][current[2] + dx[i]] == False:
            is_visited[current[0] + dz[i]][current[1] + dy[i]][current[2] + dx[i]] = True
            visited_cnt += 1
            target.append((current[0] + dz[i], current[1] + dy[i], current[2] + dx[i], current[3] + 1))

if visited_cnt + minus_cnt == M * N * H:
    print(day)

else:
    print(-1)