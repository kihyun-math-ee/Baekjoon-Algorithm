import sys
import heapq

N = int(sys.stdin.readline())
M = int(sys.stdin.readline())
is_visited = [False] * (N + 1)
is_visited[0] = True
graph = [[] for _ in range(N + 1)]

def MST(start):
    total = 0
    hq = []
    heapq.heappush(hq, (0, start))

    while hq:
        current_cost, current_node = heapq.heappop(hq)
        
        if is_visited[current_node] == True:
            continue

        is_visited[current_node] = True
        total += current_cost

        for next_node, weight in graph[current_node]:
            if is_visited[next_node] == False:
                heapq.heappush(hq, (weight, next_node))

    return total

for _ in range(M):
    A, B, C = map(int, sys.stdin.readline().split())
    graph[A].append((B, C))
    graph[B].append((A, C))


print(MST(1))
