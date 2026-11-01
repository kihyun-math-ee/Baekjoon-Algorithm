import sys
import heapq

N = int(sys.stdin.readline())

def dijkstra(start):
    hq = []
    heapq.heappush(hq, (0, start))
    distances[start] = 0
    total = 0
    num = 0

    while hq:
        current_cost, current_node = heapq.heappop(hq)

        if distances[current_node] < current_cost:
            continue

        num += 1

        for next_node, weight in graph[current_node]:
            new_cost = current_cost + weight

            if new_cost < distances[next_node]:
                distances[next_node] = new_cost
                heapq.heappush(hq, (new_cost, next_node))

    for i in range(1, n + 1):
        if distances[i] != float('inf'):
            if total < distances[i]:
                total = distances[i]

    return [num, total]

for _ in range(N):
    n, d, c = map(int, sys.stdin.readline().split())
    graph = [[] for _ in range(n + 1)]
    distances = [float('inf')] * (n + 1)
    
    for _ in range(d):
        a, b, s = map(int, sys.stdin.readline().split())
        graph[b].append((a, s))

    print(*dijkstra(c))