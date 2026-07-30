import sys
sys.setrecursionlimit(10000)

u, v = map(int, sys.stdin.readline().split())
graph = [[] * (u + 1) for _ in range(u + 1)]

for _ in range(v):
    a, b = map(int, sys.stdin.readline().split())
    graph[a].append(b)
    graph[b].append(a)

visited = [False] * (u + 1)
visited[0] = True
connected_elements = 0

def dfs(current):
    if visited[current] == True:
        return
    
    visited[current] = True
    for possible in graph[current]:
        dfs(possible)

for place in range(1, u + 1):
    if visited[place] == False:
        dfs(place)
        connected_elements += 1

print(connected_elements)