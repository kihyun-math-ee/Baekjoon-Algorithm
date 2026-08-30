import sys
from collections import deque

N = int(sys.stdin.readline())
in_degree = [0] * (N + 1)
build_time = [0] * (N + 1)
result_time = [0] * (N + 1)
graph = [[] for _ in range(N + 1)]

for i in range(1, N + 1):
    line = list(map(int, sys.stdin.readline().split()))
    build_time[i] = line[0]
    prerequisite = line[1:-1]

    for p in prerequisite:
        graph[p].append(i)
        in_degree[i] += 1

def topology_sort():
    queue = deque()

    for j in range(1, N + 1):

        if in_degree[j] == 0:
            queue.append(j)
            result_time[j] = build_time[j]

    while queue:
        current = queue.popleft()

        for next_node in graph[current]:
            result_time[next_node] = max(result_time[next_node], result_time[current] + build_time[next_node])
            in_degree[next_node] -= 1

            if in_degree[next_node] == 0:
                queue.append(next_node)

    for k in range(1, N + 1):
        print(result_time[k])

topology_sort()