import sys
import heapq

N, M = map(int, sys.stdin.readline().split())
graph = [[] for _ in range(N + 1)]
is_visited = [False] * (N + 1)
is_visited[0] = True

for _ in range(M):
    A, B, C = map(int, sys.stdin.readline().split())
    graph[A].append((B, C))
    graph[B].append((A, C))

def MST(start):
    hq = []
    heapq.heappush(hq, (0, start))
    total = 0
    max_cost = 0

    while hq:
        current_cost, current_node = heapq.heappop(hq)

        if is_visited[current_node] == True:
            continue

        is_visited[current_node] = True
        total += current_cost
        if max_cost < current_cost:
            max_cost = current_cost

        for next_node, weight in graph[current_node]:
            if is_visited[next_node] == False:
                heapq.heappush(hq, (weight, next_node))

    return (total - max_cost)

print(MST(1))