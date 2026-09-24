import sys
import heapq

def MST(start):
    hq = []
    heapq.heappush(hq, (0, start))
    mst_result = 0

    while hq:
        current_cost, current_node = heapq.heappop(hq)

        if is_visited[current_node] == True:
            continue

        is_visited[current_node] = True
        mst_result += current_cost

        for next_node, weight in graph[current_node]:
            if is_visited[next_node] == False:
                heapq.heappush(hq, (weight, next_node))

    return mst_result

while True:
    line = list(map(int, sys.stdin.readline().split()))

    if len(line) == 2:
        if line[0] == 0 and line[1] == 0:
            break

        else:
            m = line[0]
            n = line[1]
            graph = [[] for _ in range(m)]
            is_visited = [False] * (m)
            i = 0
            total = 0

    elif len(line) == 3:
        x = line[0]
        y = line[1]
        z = line[2]
        total += z
        graph[x].append((y, z))
        graph[y].append((x, z))

    if i == n:
        print(total - MST(0))

    i += 1