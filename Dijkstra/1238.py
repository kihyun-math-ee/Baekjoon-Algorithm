import sys
import heapq

N, M, X = map(int, sys.stdin.readline().split())
graph = [[] for _ in range(N + 1)]
reverse_graph = [[] for _ in range(N + 1)]

def dijkstra(start, target_graph):
    hq = []
    distances = [float('inf')] * (N + 1)
    distances[start] = 0
    heapq.heappush(hq, (0, start))

    while hq:
        current_cost, current_node = heapq.heappop(hq)

        if distances[current_node] < current_cost:
            continue

        for next_node, weight in target_graph[current_node]:
            new_cost = current_cost + weight

            if new_cost < distances[next_node]:
                distances[next_node] = new_cost
                heapq.heappush(hq, (new_cost, next_node))

    return distances

for _ in range(M):
    A, B, C = map(int, sys.stdin.readline().split())
    graph[A].append((B, C))
    reverse_graph[B].append((A, C))

go_party = dijkstra(X, reverse_graph)
go_home = dijkstra(X, graph)
max_time = 0

for i in range(1, N + 1):
    total = go_party[i] + go_home[i]

    if total > max_time:
        max_time = total

print(max_time)