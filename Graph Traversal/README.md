# Graph Traversal

This folder contains 10 BOJ solution files. Dates are the earliest recorded study dates in the original Study Log.

## 📅 Study Log

| Date | Category | Problem | Key Learnings |
| :--- | :--- | :--- | :--- |
| 2026-07-17 | Graph Traversal | 1697 | Implemented breadth-first search using collections.deque to calculate the shortest time. Tracked the current position and elapsed time as tuples in the queue, utilizing a visited array to prevent redundant explorations and infinite loops. |
| 2026-07-18 | Graph Traversal | 1260 | Implemented and compared Depth-First Search and Breadth-First Search using an adjacency list. Sorted the adjacent nodes in ascending order prior to exploration to satisfy the specific traversal condition. Utilized recursion for DFS and collections.deque for BFS. |
| 2026-07-19 | Graph Traversal | 10026 | Implemented Depth-First Search to count connected components in a 2D grid. Applied conditional branching within the DFS engine to simultaneously simulate normal and red-green colorblind vision. Utilized matrix padding to eliminate boundary checks and adjusted Python's recursion limit to prevent runtime errors. |
| 2026-07-21 | Graph Traversal | 2178 | Implemented a BFS algorithm using deque to find the shortest path in a 2D maze. Applied a 1-layer zero-padding technique to the grid to efficiently eliminate out-of-bounds checks during 4-directional movement. |
| 2026-07-31 | Graph Traversal | 11724 | Implemented a Depth-First Search (DFS) algorithm to find and count connected components in a given undirected graph. Prevented potential runtime errors by preemptively increasing Python's default recursion depth limit. |
| 2026-08-01 | Graph Traversal | 7569 | Implemented a 3D Breadth-First Search (BFS) using deque to track the minimum days required for tomatoes to ripen across multiple layers. Applied a boundary padding technique (surrounding the 3D grid with -1) to efficiently prevent index out-of-bounds errors and optimize directional checks. |
| 2026-08-20 | Graph Traversal | 2206 | Implemented a Breadth-First Search (BFS) algorithm to find the shortest path in a grid where up to one wall can be broken. Utilized a 3D visited array to independently track the state of paths that have and haven't broken a wall. Applied a boundary padding technique to the grid and visited array to optimize execution by eliminating redundant out-of-bounds branching during traversal. |
| 2026-08-23 | Graph Traversal | 2468 | Implemented Depth-First Search (DFS) to calculate the maximum number of safe areas across all possible water levels. Optimized grid traversal by applying a 0-padding boundary strategy to eliminate redundant out-of-bounds checks. Safely managed Python's recursion depth overhead using `sys.setrecursionlimit`. |
| 2026-09-08 | Graph Traversal | 2667 | Used BFS to count connected housing components in a padded 2D grid. |
| 2026-09-09 | Graph Traversal | 7562 | Used BFS with a deque to find the shortest knight path on a padded chessboard. |
