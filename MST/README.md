# MST

This folder contains 7 BOJ solution files. Dates are the earliest recorded study dates in the original Study Log.

## 📅 Study Log

| Date | Category | Problem | Key Learnings |
| :--- | :--- | :--- | :--- |
| 2026-08-05 | MST | 1197 | Implemented Kruskal's algorithm to find the Minimum Spanning Tree. Mastered the Union-Find (Disjoint Set) data structure using path compression in find_parent to efficiently detect and prevent graph cycles. |
| 2026-08-08 | MST | 1647 | Implemented Prim's algorithm using a priority queue to construct a Minimum Spanning Tree (MST). Successfully solved the problem of dividing a city into two optimized components by tracking and subtracting the maximum edge weight from the total MST cost. |
| 2026-08-15 | MST | 1833 | Implemented Prim's algorithm using a priority queue to construct a Minimum Spanning Tree (MST). Effectively handled pre-connected edges (negative weights) by absorbing their absolute costs in advance and assigning them a weight of zero in the graph, outputting both the total cost and the specific newly constructed paths. |
| 2026-08-18 | MST | 1922 | Implemented Prim's algorithm using a priority queue (`heapq`) to construct a Minimum Spanning Tree (MST). Efficiently calculated the minimum total cost to connect all nodes while preventing cycles through a boolean visited array, achieving an optimal $O(E \log V)$ time complexity. |
| 2026-09-17 | MST | 1774 | Implemented Kruskal's algorithm powered by a Union-Find (Disjoint Set) engine with path compression to construct a Minimum Spanning Tree on 2D coordinates. Pre-merged initially connected components via disjoint sets, generated all candidate Euclidean edges, and greedily selected minimum-cost edges to compute the minimal additional connection cost. |
| 2026-09-19 | MST | 2887 | Reduced candidate edge space from $O(N^2)$ to $3(N-1)$ by sorting spatial coordinates independently across $X, Y, Z$ axes. Implemented Kruskal's algorithm backed by a path-compressed Disjoint Set to connect 3D celestial coordinates with minimal tunneling cost in $O(N \log N)$ time. |
| 2026-09-22 | MST | 4386 | Modeled 2D celestial coordinates as a complete Euclidean graph and implemented Kruskal's algorithm backed by a path-compressed Disjoint Set. Generated all $O(N^2)$ candidate distances, sorted edges in ascending order, and greedily selected acyclic connections to determine the minimum cost to form a constellation in $O(N^2 \log N)$ time. |
