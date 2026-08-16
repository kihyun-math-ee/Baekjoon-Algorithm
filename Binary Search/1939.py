import sys
from collections import deque

N, M = map(int, sys.stdin.readline().split())
graph = [[] for _ in range(N + 1)]

for _ in range(M):
    A, B, C = map(int, sys.stdin.readline().split())
    graph[A].append((B, C))
    graph[B].append((A, C))

start_factory, end_factory = map(int, sys.stdin.readline().split())

def bfs(target_weight):
    queue = deque([start_factory])
    is_visited = [False] * (N + 1)
    is_visited[start_factory] = True

    while queue:
        current_node = queue.popleft()

        if current_node == end_factory:
            return True

        for next_node, weight in graph[current_node]:
            if is_visited[next_node] == False:
                if weight >= target_weight:
                    is_visited[next_node] = True
                    queue.append(next_node)

    return False

low = 1
high = 1000000000
answer = 0

while low <= high:
    mid = (high + low) // 2

    if bfs(mid):
        answer = mid
        low = mid + 1

    else:
        high = mid - 1

print(answer)