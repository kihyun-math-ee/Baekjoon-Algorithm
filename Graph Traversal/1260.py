import sys
from collections import deque

target_bfs = deque()

N, M, V = map(int, sys.stdin.readline().split())
graph = [[] * (N + 1) for _ in range(N + 1)]
visited_bfs = [False] * (N + 1)
visited_bfs[0] = True
visited_dfs = [False] * (N + 1)
visited_dfs[0] = True
bfs_route = []
dfs_route = []

for _ in range(M):
    A, B = map(int, sys.stdin.readline().split())
    graph[A].append(B)
    graph[B].append(A)

for row in range(1, N + 1):
    graph[row].sort()

target_bfs.append(V)

while target_bfs:
    current_bfs = target_bfs.popleft()
    if visited_bfs[current_bfs] == False:
        bfs_route.append(current_bfs)
        visited_bfs[current_bfs] = True
        for j in range(len(graph[current_bfs])):
            target_bfs.append(graph[current_bfs][j])

def dfs(current_dfs):
    if visited_dfs[current_dfs] == True:
        return
    
    visited_dfs[current_dfs] = True
    dfs_route.append(current_dfs)
    for next_node in graph[current_dfs]:
        dfs(next_node)

dfs(V)

print(*dfs_route)
print(*bfs_route)