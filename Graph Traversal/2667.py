import sys
from collections import deque

target = deque()
N = int(sys.stdin.readline())
L = [[0] * (N + 2)]

for _ in range(N):
    line = sys.stdin.readline().strip()
    row = list(map(int, line))
    row = [0] + row + [0]
    L.append(row)

L.append([0] * (N + 2))

visited = [[True] * (N + 2)]
for j in range(1, N + 1):
    visited.append([False] * (N + 2))
visited.append([True] * (N + 2))
complex_num = 0
houses_list = []

for i in range(1, N + 1):
    visited[i][0] = True
    visited[i][N + 1] = True

for y in range(1, N + 1):
    for x in range(1, N + 1):
        if L[y][x] == 1:
            if visited[y][x] == False:
                visited[y][x] = True
                target.append((y, x))
                complex_num += 1
                houses_num = 1
                while target:
                    current = target.popleft()
                    
                    if L[current[0] + 1][current[1]] == 1:
                        if visited[current[0] + 1][current[1]] == False:
                            visited[current[0] + 1][current[1]] = True
                            target.append((current[0] + 1, current[1]))
                            houses_num += 1
                    
                    if L[current[0]][current[1] + 1] == 1:
                        if visited[current[0]][current[1] + 1] == False:
                            visited[current[0]][current[1] + 1] = True
                            target.append((current[0], current[1] + 1))
                            houses_num += 1

                    if L[current[0] - 1][current[1]] == 1:
                        if visited[current[0] - 1][current[1]] == False:
                            visited[current[0] - 1][current[1]] = True
                            target.append((current[0] - 1, current[1]))
                            houses_num += 1
                                        
                    if L[current[0]][current[1] - 1] == 1:
                        if visited[current[0]][current[1] - 1] == False:
                            visited[current[0]][current[1] - 1] = True
                            target.append((current[0], current[1] - 1))
                            houses_num += 1
                
                houses_list.append(houses_num)

houses_list.sort()
print(complex_num)

for num in houses_list:
    print(num)