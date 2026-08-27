import sys
import heapq

dy = [1, -1, 0, 0]
dx = [0, 0, 1, -1]
num = 1

def dijkstra(start_y, start_x):
    hq = []
    heapq.heappush(hq, (L[start_y][start_x], start_y, start_x))
    distances[start_y][start_x] = L[start_y][start_x]

    while hq:
        current_cost, current_y, current_x = heapq.heappop(hq)

        if distances[current_y][current_x] < current_cost:
            continue

        for i in range(4):
            new_cost = current_cost + L[current_y + dy[i]][current_x + dx[i]]
            if new_cost < distances[current_y + dy[i]][current_x + dx[i]]:
                distances[current_y + dy[i]][current_x + dx[i]] = new_cost
                heapq.heappush(hq, (new_cost, current_y + dy[i], current_x + dx[i]))

while True:
    N = int(sys.stdin.readline())

    if N == 0:
        break

    else:
        L = [[float('inf')] * (N + 2)]

        for _ in range(N):
            row = list(map(int, sys.stdin.readline().split()))
            row = [float('inf')] + row + [float('inf')]
            L.append(row)

        L.append([float('inf')] * (N + 2))

        distances = [[float('inf')] * (N + 2) for _ in range(N + 2)]

        dijkstra(1, 1)
        print(f"Problem {num}: {distances[N][N]}")
        num += 1