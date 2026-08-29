import sys
from collections import deque

T = int(sys.stdin.readline())

for _ in range(T):
    N, K = map(int, sys.stdin.readline().split())
    L = list(map(int, sys.stdin.readline().split()))
    L = [0] + L
    graph = [[] for _ in range(N + 1)]
    in_degree = [0] * (N + 1)
    queue = deque()
    result_time = [0] * (N + 1)

    for _ in range(K):
        X, Y = map(int, sys.stdin.readline().split())
        graph[X].append(Y)
        in_degree[Y] += 1

    for i in range(1, N + 1):
        if in_degree[i] == 0:
            queue.append(i)
            result_time[i] = L[i]

    while queue:
        current = queue.popleft()

        for next_node in graph[current]:
            result_time[next_node] = max(result_time[next_node], result_time[current] + L[next_node])
            in_degree[next_node] -= 1

            if in_degree[next_node] == 0:
                queue.append(next_node)

    target = int(sys.stdin.readline())
    print(result_time[target])