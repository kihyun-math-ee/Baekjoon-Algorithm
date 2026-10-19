# Topological Sort

This folder contains 6 BOJ solution files. Existing dates follow the original Study Log; new entries use the archive date.

## 📅 Study Log

| Date | Category | Problem | Key Learnings |
| :--- | :--- | :--- | :--- |
| 2026-08-30 | Topological Sort | 1005 | Implemented Topological Sort using a deque to manage complex building prerequisite chains. Combined with Dynamic Programming to accumulate the maximum required build time (`result_time[next_node] = max(...)`) across multiple incoming edge paths, efficiently resolving the bottlenecks in $O(V+E)$ time complexity. |
| 2026-08-31 | Topological Sort | 1516 | Solved parallel construction constraints on a Directed Acyclic Graph (DAG) using Topological Sort. Merged DP state transition (result_time[next] = max(result_time[next], result_time[current] + build_time[next])) to track the maximum cumulative time of prerequisites. Utilized 1D arrays for in-degrees and timing to ensure optimal cache locality, achieving O(V + E) complexity. |
| 2026-09-03 | Topological Sort | 2252 | Implemented Kahn's algorithm for topological sorting on a Directed Acyclic Graph (DAG). Utilized an adjacency list and in-degree array to track node prerequisites, effectively resolving the ordering sequence in $O(V+E)$ time complexity. Optimized BFS queue operations by adopting collections.deque to prevent the memory shift overheads of standard lists. |
| 2026-09-23 | Topological Sort | 1766 | Implemented Kahn's algorithm for topological sorting augmented with a min-heap (`heapq`). Resolved prerequisite dependencies via in-degree tracking while greedily selecting the lowest-indexed candidate among zero in-degree nodes in $O((V + E) \log V)$ time. |
| 2026-10-18 | Topological Sort | 2623 | Converted each producer's ordered singer sequence into directed edges between consecutive singers. Applied Kahn's algorithm with an in-degree array and `collections.deque` to print a valid full order, or `0` when a cycle prevents all singers from being processed, in O(N + M + E) time for N singers, M sequences, and E precedence edges. |
| 2026-10-20 | Topological Sort | 2056 | Applied Kahn's Topological Sort with an in-degree array and `collections.deque` to process prerequisite tasks. Propagated the maximum predecessor completion time to each dependent task and returned the latest completion time, using O(N + E) time and space. |
