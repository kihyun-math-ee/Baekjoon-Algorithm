import sys
import heapq

N = int(sys.stdin.readline())
zone = [[float('inf')] * (503)]

for _ in range(501):
    zone.append([float('inf')] + [0] * (501) + [float('inf')])

zone.append([float('inf')] * (503))
distances = [[float('inf')] * (503) for _ in range(503)]
dy = [1, -1, 0, 0]
dx = [0, 0, 1, -1]

for _ in range(N):
    X1, Y1, X2, Y2 = map(int, sys.stdin.readline().split())
    for y in range(min(Y1 + 1, Y2 + 1), max(Y1 + 1, Y2 + 1) + 1):
        for x in range(min(X1 + 1, X2 + 1), max(X1 + 1, X2 + 1) + 1):
            zone[y][x] = 1

M = int(sys.stdin.readline())

for _ in range(M):
    X1, Y1, X2, Y2 = map(int, sys.stdin.readline().split())
    for i in range(min(Y1 + 1, Y2 + 1), max(Y1 + 1, Y2 + 1) + 1):
        for j in range(min(X1 + 1, X2 + 1), max(X1 + 1, X2 + 1) + 1):
            zone[i][j] = float('inf')

def dijkstra(start_y, start_x):
    hq = []
    heapq.heappush(hq, (0, start_y, start_x))
    distances[start_y][start_x] = 0

    while hq:
        current_cost, current_y, current_x = heapq.heappop(hq)

        if distances[current_y][current_x] < current_cost:
            continue

        distances[current_y][current_x] = current_cost

        for k in range(4):
            weight = zone[current_y + dy[k]][current_x + dx[k]]
            if current_cost + weight < distances[current_y + dy[k]][current_x + dx[k]]:
                distances[current_y + dy[k]][current_x + dx[k]] = current_cost + weight
                heapq.heappush(hq, (current_cost + weight, current_y + dy[k], current_x + dx[k]))

    if distances[501][501] == float('inf'):
        return -1

    else:
        return distances[501][501]
    
print(dijkstra(1, 1))


            
    