import sys
import heapq

N, M = map(int, sys.stdin.readline().split())
graph = [[] for _ in range(N + 1)]
distances = [float('inf')] * (N + 1)

def dijkstra(start):
    hq = []
    heapq.heappush(hq, (0, start))
    distances[start] = 0
    
    while hq:
        current_cost, current_node = heapq.heappop(hq)

        if distances[current_node] < current_cost:
            continue

        for next_node, weight in graph[current_node]:
            new_cost = current_cost + weight

            if new_cost < distances[next_node]:
                distances[next_node] = new_cost
                heapq.heappush(hq, (new_cost, next_node))

for _ in range(M):
    A, B, C = map(int, sys.stdin.readline().split())
    graph[A].append((B, C))
    graph[B].append((A, C))

dijkstra(1)
print(distances[N])