import sys
import heapq

V, R, C = map(int, sys.stdin.readline().split())
time = [[float('inf')] * (C + 2) for _ in range(R + 2)]
L = [[float('inf')] * (C + 2)]
dy = [1, -1, 0, 0]
dx = [0, 0, 1, -1]

for _ in range(R):
    row = list(map(int, sys.stdin.readline().split()))
    row = [float('inf')] + row + [float('inf')]
    L.append(row)

L.append([float('inf')] * (C + 2))

def dijkstra(start_y, start_x):
    hq = []
    heapq.heappush(hq, (0, start_y, start_x))
    time[start_y][start_x] = 0

    while hq:
        current_cost, current_y, current_x = heapq.heappop(hq)

        if time[current_y][current_x] < current_cost:
            continue

        A = L[current_y][current_x]

        for i in range(4):
            if L[current_y + dy[i]][current_x + dx[i]] != float('inf'):
                new_cost = current_cost + (2 ** (A - L[start_y][start_x])) / V
                if new_cost < time[current_y + dy[i]][current_x + dx[i]]:
                    time[current_y + dy[i]][current_x + dx[i]] = new_cost
                    heapq.heappush(hq, (new_cost, current_y + dy[i], current_x + dx[i]))

    return time[R][C]

print(f"{dijkstra(1, 1):.2f}")
        