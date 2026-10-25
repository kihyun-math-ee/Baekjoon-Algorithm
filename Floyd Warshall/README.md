# Floyd Warshall

This folder contains 6 BOJ solution files. Existing dates follow the original Study Log; new entries use the archive date.

## 📅 Study Log

| Date | Category | Problem | Key Learnings |
| :--- | :--- | :--- | :--- |
| 2026-09-11 | Floyd Warshall | 2458 | Implemented the Floyd-Warshall algorithm to compute the all-pairs reachability matrix in a directed graph. Accurately determined the exact topological rank of each node by verifying if the count of its incoming and outgoing paths equals N - 1, successfully managing the $O(N^3)$ time complexity. |
| 2026-09-12 | Floyd Warshall | 11780 | Implemented the Floyd-Warshall algorithm to compute all-pairs shortest paths and reconstruct the exact traversal paths. Engineered a next-node routing table (`nxt`) updated dynamically during the $O(N^3)$ relaxation phase, enabling efficient $O(V)$ path reconstruction while handling multiple edges by tracking minimal weights. |
| 2026-09-13 | Floyd Warshall | 11404 | Implemented the Floyd-Warshall algorithm to compute the all-pairs shortest paths in a directed graph. Constructed an $O(N^2)$ adjacency matrix and accurately handled parallel edges by strictly keeping the minimum weight. Applied the $O(N^3)$ relaxation logic to evaluate intermediate paths, successfully converting unreachable paths to zero for the final output. |
| 2026-09-14 | Floyd Warshall | 11403 | Implemented the Floyd-Warshall algorithm to compute the transitive closure of a directed graph. Optimized the $O(N^3)$ relaxation phase by using simple boolean logic checks (`graph[i][k] == 1 and graph[k][j] == 1`) instead of arithmetic distance tracking, accurately determining the reachability between all pairs of nodes. |
| 2026-09-15 | Floyd Warshall | 14938 | Implemented the Floyd-Warshall algorithm to evaluate all-pairs shortest paths on an undirected graph. Handled parallel edges by tracking minimum edge weights, accurately checked search radius boundaries (`graph[y][x] <= m`) from each drop point, and optimized total item harvesting within an efficient $O(N^3)$ time complexity. |
| 2026-10-26 | Floyd Warshall | 1389 | Applied Floyd-Warshall to an undirected friendship graph to compute all-pairs shortest distances in $O(N^3)$ time and $O(N^2)$ space. Summed each user's distances and selected the lowest-indexed user on ties by updating the result only for a strictly smaller total. |
