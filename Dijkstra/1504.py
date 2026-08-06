import sys
import heapq

N, E = map(int, sys.stdin.readline().split())
graph = [[] for _ in range(N + 1)]

def dijkstra(start):
    hq = []
    distance = [float('inf')] * (N + 1)
    heapq.heappush(hq, (0, start))
    distance[start] = 0

    while hq:
        current_cost, current_node = heapq.heappop(hq)

        if distance[current_node] < current_cost:
            continue

        for next_node, weight in graph[current_node]:
            new_cost = current_cost + weight
            if new_cost < distance[next_node]:
                distance[next_node] = new_cost
                heapq.heappush(hq, (new_cost, next_node))

    return distance

for _ in range(E):
    A, B, C = map(int, sys.stdin.readline().split())
    graph[A].append((B, C))
    graph[B].append((A, C))

v1, v2 = map(int, sys.stdin.readline().split())

dist_from_1 = dijkstra(1)
dist_from_v1 = dijkstra(v1)
dist_from_v2 = dijkstra(v2)

route_A = dist_from_1[v1] + dist_from_v1[v2] + dist_from_v2[N]
route_B = dist_from_1[v2] + dist_from_v2[v1] + dist_from_v1[N]

final_cost = min(route_A, route_B)

if final_cost == float('inf'):
    print(-1)

else:
    print(final_cost)