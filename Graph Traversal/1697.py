import sys
from collections import deque

N, K = map(int, sys.stdin.readline().split())
L = deque()
visited = [False] * 100001
L.append((N, 0))
visited[N] = True

while L:
    current_pos, current_time = L.popleft()
    
    if current_pos == K:
        print(current_time)
        break

    for next_pos in (current_pos - 1, current_pos + 1, current_pos * 2):
        if 0 <= next_pos <= 100000 and not visited[next_pos]:
            visited[next_pos] = True
            L.append((next_pos, current_time + 1))