import sys
import heapq

N = int(sys.stdin.readline())
is_visited = [False] * (N + 2)
is_visited[0] = True
is_visited[N + 1] = True
graph = [[] for _ in range(N + 1)]
previous_cost = 0

for i in range(1, N + 1):
    line = list(map(int, sys.stdin.readline().split()))
    line = [0] + line

    for j in range(1, N + 1):

        if line[j] < 0:
            graph[i].append((j, 0))
            previous_cost += abs(line[j])
        elif line[j] > 0: 
            graph[i].append((j, line[j]))

previous_cost //= 2

def MST(start):
    global previous_cost
    hq = []
    heapq.heappush(hq, (0, start, start))
    total = 0
    total += previous_cost
    num = 0
    build_list = []

    while hq:
        current_cost, current_node, past_node = heapq.heappop(hq)

        if is_visited[current_node] == True:
            continue

        is_visited[current_node] = True
        if current_cost > 0 and current_cost != float('inf'):
            num += 1
            build_list.append([past_node, current_node])

        total += current_cost

        for next_node, weight in graph[current_node]:
            if is_visited[next_node] == False:
                heapq.heappush(hq, (weight, next_node, current_node))

    print(total, num)
    for l in range(len(build_list)):
        print(*build_list[l])

MST(1)