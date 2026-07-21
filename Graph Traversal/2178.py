import sys
from collections import deque

N, M = map(int, sys.stdin.readline().split())
L = [[0] * (M + 2)]
target = deque()
target.append((1, 1, 1))

for _ in range(N):
    row = sys.stdin.readline().strip()
    row = list(map(int, row))
    row = [0] + row + [0]
    L.append(row)

L.append([0] * (M + 2))
visited = [[False] * (M + 2) for _ in range(N + 2)]
visited[1][1] = True

while target:
    current_pos = target.popleft()
    if current_pos[0] == N and current_pos[1] == M:
        print(current_pos[2])
        break

    if L[current_pos[0] + 1][current_pos[1]] == 1 and visited[current_pos[0] + 1][current_pos[1]] == False:
        target.append((current_pos[0] + 1, current_pos[1], current_pos[2] + 1))
        visited[current_pos[0] + 1][current_pos[1]] = True

    if L[current_pos[0]][current_pos[1] + 1] == 1 and visited[current_pos[0]][current_pos[1] + 1] == False:
        target.append((current_pos[0], current_pos[1] + 1, current_pos[2] + 1))
        visited[current_pos[0]][current_pos[1] + 1] = True

    if L[current_pos[0] - 1][current_pos[1]] == 1 and visited[current_pos[0] - 1][current_pos[1]] == False:
        target.append((current_pos[0] - 1, current_pos[1], current_pos[2] + 1))
        visited[current_pos[0] - 1][current_pos[1]] = True

    if L[current_pos[0]][current_pos[1] - 1] == 1 and visited[current_pos[0]][current_pos[1] - 1] == False:
        target.append((current_pos[0], current_pos[1] - 1, current_pos[2] + 1))
        visited[current_pos[0]][current_pos[1] - 1] = True
