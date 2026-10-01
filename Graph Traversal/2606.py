import sys

N = int(sys.stdin.readline())
line = int(sys.stdin.readline())
graph = [[] for _ in range(N + 1)]

for _ in range(line):
    A, B = map(int, sys.stdin.readline().split())
    graph[A].append(B)
    graph[B].append(A)

visited = [False] * (N + 1)

def dfs(current):
    visited[current] = True
    
    for next_node in graph[current]:
        if not visited[next_node]:
            dfs(next_node)

dfs(1)

print(sum(visited) - 1)

