import sys
import heapq

n, m = map(int, sys.stdin.readline().split())
distances = [float('inf')] * (n + 1)
graph = [[] for _ in range(n + 1)]

def digkstra(start):
    hq = []
    distances[start] = 0
    heapq.heappush(hq, (0, start))

    while hq:
        current_cost, current_node = heapq.heappop(hq)

        if distances[current_node] < current_cost:
            continue

        for next_node, weight in graph[current_node]:
            new_cost = current_cost + weight

            if new_cost < distances[next_node]:
                distances[next_node] = new_cost
                heapq.heappush(hq, (new_cost, next_node))

for _ in range(m):
    A, B, C = map(int, sys.stdin.readline().split())
    graph[A].append((B, C))
    graph[B].append((A, C))

s, t = map(int, sys.stdin.readline().split())
digkstra(s)
print(distances[t])