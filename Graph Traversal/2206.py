import sys
import copy
from collections import deque

N, M = map(int, sys.stdin.readline().split())
target = deque()
L = [[1] * (M + 2)]

for _ in range(N):
    S = sys.stdin.readline().strip()
    S = list(map(int, S))
    row = [1] + S + [1]
    L.append(row)

L.append([1] * (M + 2))
is_visited = [[True] * (M + 2)] 

for _ in range(1, N + 1):
    visit_row = [False] * M
    visit_row = [True] + visit_row + [True]
    is_visited.append(visit_row)

is_visited.append([True] * (M + 2))
is_visited = [copy.deepcopy(is_visited) for _ in range(2)]
target.append((1, 1, 0, 1))
is_visited[0][1][1] = True
dy = [1, -1, 0, 0]
dx = [0, 0, 1, -1]
is_possible = False

while target:
    current = target.popleft()
    if current[0] == N and current[1] == M:
        print(current[3])
        is_possible = True
        break

    if current[2] == 1:
        for i in range(4):
            if is_visited[1][current[0] + dy[i]][current[1] + dx[i]] == False and L[current[0] + dy[i]][current[1] + dx[i]] == 0:
                is_visited[1][current[0] + dy[i]][current[1] + dx[i]] = True
                target.append((current[0] + dy[i], current[1] + dx[i], 1, current[3] + 1))

    else:
        for i in range(4):
            if is_visited[0][current[0] + dy[i]][current[1] + dx[i]] == False and L[current[0] + dy[i]][current[1] + dx[i]] == 0:
                is_visited[0][current[0] + dy[i]][current[1] + dx[i]] = True
                target.append((current[0] + dy[i], current[1] + dx[i], 0, current[3] + 1))

            elif is_visited[1][current[0] + dy[i]][current[1] + dx[i]] == False and L[current[0] + dy[i]][current[1] + dx[i]] == 1:
                is_visited[1][current[0] + dy[i]][current[1] + dx[i]] = True
                target.append((current[0] + dy[i], current[1] + dx[i], 1, current[3] + 1))

if not is_possible:
    print(-1)