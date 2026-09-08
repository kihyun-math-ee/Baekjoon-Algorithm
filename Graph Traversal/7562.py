import sys
from collections import deque

T = int(sys.stdin.readline())
dy = [2, 1, -1, -2, -2, -1, 1, 2]
dx = [1, 2, 2, 1, -1, -2, -2, -1]

for _ in range(T):
    target = deque()
    N = int(sys.stdin.readline())
    is_visited = [[True] * (N + 4), [True] * (N + 4)]
    
    for _ in range(N):
        is_visited.append(([True] * 2) + ([False] * N) + ([True] * 2))
    
    is_visited.append([True] * (N + 4))
    is_visited.append([True] * (N + 4))
    start_y, start_x = map(int, sys.stdin.readline().split())
    start_y = start_y + 2
    start_x = start_x + 2
    end_y, end_x = map(int, sys.stdin.readline().split())
    end_y = end_y + 2
    end_x = end_x + 2
    is_visited[start_y][start_x] = True
    target.append((start_y, start_x, 0))
    
    while target:
        current = target.popleft()
        
        if current[0] == end_y and current[1] == end_x:
            print(current[2])
            break
        
        for i in range(8):
            if is_visited[current[0] + dy[i]][current[1] + dx[i]] == False:
                is_visited[current[0] + dy[i]][current[1] + dx[i]] = True
                target.append((current[0] + dy[i], current[1] + dx[i], current[2] + 1))