import sys
from collections import deque

N = int(sys.stdin.readline())
in_degree = [0] * (N + 1)
build_time = [0] * (N + 1)
result_time = [0] * (N + 1)
graph = [[] for _ in range(N + 1)]
q = deque()

for i in range(1, N + 1):
    L = list(map(int, sys.stdin.readline().split()))
    build_time[i] = L[0]

    if L[1] == 0:
        result_time[i] = L[0]
        q.append(i)

    else:
        in_degree[i] = L[1]

        for j in range(2, 2 + L[1]):
            graph[L[j]].append(i)

while q:
    current = q.popleft()

    for next_node in graph[current]:
        in_degree[next_node] -= 1
        result_time[next_node] = max(result_time[next_node], result_time[current] + build_time[next_node])

        if in_degree[next_node] == 0:
            q.append(next_node)

print(max(result_time))