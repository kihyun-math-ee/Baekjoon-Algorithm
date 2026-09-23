# Dijkstra

This folder contains 10 BOJ solution files. Dates are the earliest recorded study dates in the original Study Log.

## 📅 Study Log

| Date | Category | Problem | Key Learnings |
| :--- | :--- | :--- | :--- |
| 2026-07-29 | Dijkstra | 14284 | Implemented standard Dijkstra's algorithm using a priority queue (Min-Heap) to efficiently calculate the minimum cost path between a specific start and target node in an undirected graph. |
| 2026-08-04 | Dijkstra | 1238 | Solved the "Party" problem by implementing Dijkstra's algorithm. Optimized the round-trip shortest path calculation from $O(N \cdot E \log V)$ to $O(E \log V)$ by successfully utilizing a reverse graph for incoming paths to the target node. |
| 2026-08-06 | Dijkstra | 1261 | Minimized wall-breaking costs in a 2D grid using Dijkstra's algorithm with a priority queue and optimized boundary checks via infinity padding. |
| 2026-08-07 | Dijkstra | 1504 | Calculated the minimum cost path traversing two specific nodes by executing Dijkstra's algorithm three times (from start, v1, and v2) and comparing the two possible route permutations. |
| 2026-08-08 | Dijkstra | 1584 | Implemented Dijkstra's algorithm on a 2D grid using a priority queue. Applied a padding technique with `float('inf')` boundaries to elegantly handle index out-of-bounds. Effectively calculated the minimum cost path navigating through safe (0), danger (1), and death (inf) zones. |
| 2026-08-11 | Dijkstra | 1753 | Implemented standard Dijkstra's algorithm using a priority queue (`heapq`) to find the shortest paths from a single starting node. Efficiently managed edge weights and avoided redundant distance updates with a pruning condition (`if distances[node] < cost: continue`). Handled unreachable nodes by outputting 'INF'. |
| 2026-08-16 | Dijkstra | 1916 | Implemented Dijkstra's algorithm using a priority queue (`heapq`) to calculate the minimum cost path from a starting node to a destination node. Optimized the time complexity to $O(E \log V)$ by employing a relaxation check (`distances[current_node] < current_cost`) to skip redundant operations on already processed nodes. |
| 2026-08-19 | Dijkstra | 2158 | Implemented Dijkstra's algorithm using a priority queue (`heapq`) to find the path with the minimum time traversal on a 2D grid. Applied a boundary padding technique using `float('inf')` to eliminate redundant bounds-checking branches during traversal, optimizing the execution speed. Successfully processed dynamic edge weights based on elevation differences and velocity, formatting the final result to two decimal places. |
| 2026-08-28 | Dijkstra | 4485 | Implemented Dijkstra's algorithm with a priority queue to find the minimum cost path in a 2D grid. Optimized grid traversal by padding the matrix boundaries with infinite weights, effectively eliminating conditional branching overhead for out-of-bounds checks. |
| 2026-09-10 | Dijkstra | 5972 | Implemented Dijkstra's algorithm using a priority queue (`heapq`) to find the minimum cost path in an undirected graph. Optimized the traversal process by explicitly filtering out outdated paths from the heap, successfully achieving an efficient $O(E \log V)$ time complexity. |
