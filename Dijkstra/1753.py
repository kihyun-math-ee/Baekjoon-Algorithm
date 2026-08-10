import sys
import heapq

V, E = map(int, sys.stdin.readline().split())
K = int(sys.stdin.readline())
graph = [[] for _ in range(V + 1)]
distances = [float('inf')] * (V + 1)

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

for _ in range(E):
    u, v, w = map(int, sys.stdin.readline().split())
    graph[u].append((v, w))

dijkstra(K)

for i in range(1, V + 1):
    if distances[i] == float('inf'):
        print('INF')
    else:
        print(distances[i])