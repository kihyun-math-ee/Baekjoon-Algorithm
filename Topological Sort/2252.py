import sys
from collections import deque

N, M = map(int, sys.stdin.readline().split())
in_degree = [0] * (N + 1)
graph = [[] for _ in range(N + 1)]

for _ in range(M):
    A, B = map(int, sys.stdin.readline().split())
    graph[A].append(B)
    in_degree[B] += 1

def topology_sort():
    result = []
    queue = deque()

    for i in range(1, N + 1):
        if in_degree[i] == 0:
            queue.append(i)

    while queue:
        current = queue.popleft()
        result.append(current)

        for next_node in graph[current]:
            in_degree[next_node] -= 1

            if in_degree[next_node] == 0:
                queue.append(next_node)

    for res in result:
        print(res, end=' ')

topology_sort()