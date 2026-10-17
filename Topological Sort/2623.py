import sys
from collections import deque

N, M = map(int, sys.stdin.readline().split())
in_degree = [0] * (N + 1)
graph = [[] for _ in range(N + 1)]

for _ in range(M):
    line = list(map(int, sys.stdin.readline().split()))

    for j in range(1, line[0]):
        graph[line[j]].append(line[j + 1])
        in_degree[line[j + 1]] += 1

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

    if len(result) < N:
        print(0)
    else:
        for k in range(len(result)):
            print(result[k])

topology_sort()