import sys
import heapq

N, M = map(int, sys.stdin.readline().split())
in_degree = [0] * (N + 1)
graph = [[] for _ in range(N + 1)]

for _ in range(M):
    A, B = map(int, sys.stdin.readline().split())
    graph[A].append(B)
    in_degree[B] += 1

queue = []
result = []

for i in range(1, N + 1):
    if in_degree[i] == 0:
        heapq.heappush(queue, i)

while queue:
    current = heapq.heappop(queue)
    result.append(current)

    for next_node in graph[current]:
        in_degree[next_node] -= 1

        if in_degree[next_node] == 0:
            heapq.heappush(queue, next_node)
            
print(*result)