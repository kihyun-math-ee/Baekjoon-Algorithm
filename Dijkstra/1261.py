import sys
import heapq

M, N = map(int, sys.stdin.readline().split())
dy = [1, -1, 0, 0]
dx = [0, 0, 1, -1]
distances = [[float('inf')] * (M + 2) for _ in range(N + 2)]
L = [[float('inf')] * (M + 2)]
for _ in range(N):
    S = sys.stdin.readline().strip()
    row = list(map(int, S))
    row = [float('inf')] + row + [float('inf')]
    L.append(row)

L.append([float('inf')] * (M + 2))



def dijkstra(start_y, start_x):
    hq = []
    heapq.heappush(hq, (0, start_y, start_x))
    distances[start_y][start_x] = 0

    while hq:
        current_cost, current_y, current_x = heapq.heappop(hq)

        if distances[current_y][current_x] < current_cost:
            continue

        for i in range(4):
            next_y = current_y + dy[i]
            next_x = current_x + dx[i]
            new_cost = current_cost + L[next_y][next_x]
            
            if new_cost < distances[next_y][next_x]:
                distances[next_y][next_x] = new_cost
                heapq.heappush(hq, (new_cost, next_y, next_x))

dijkstra(1, 1)
print(distances[N][M])