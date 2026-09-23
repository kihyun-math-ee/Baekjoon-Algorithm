# Prefix Sum

This folder contains 5 BOJ solution files. Dates are the earliest recorded study dates in the original Study Log.

## 📅 Study Log

| Date | Category | Problem | Key Learnings |
| :--- | :--- | :--- | :--- |
| 2026-07-09 | Prefix Sum | 13900 | Optimized the sum of all pairwise products to O(N) time complexity by replacing O(N^2) combinations with O(1) prefix sum queries. |
| 2026-07-22 | Prefix Sum | 31801 | Precomputed mountain-shaped numbers using Backtracking (DFS), but the core optimization was building a Prefix Sum array to process $T$ range queries in $O(1)$ time, effectively preventing Time Limit Exceeded (TLE). |
| 2026-07-23 | Prefix Sum | 31563 | Optimized circular array rotation queries to $O(1)$ time by tracking the relative start index with modulo arithmetic instead of physical shifting. Handled wrap-around range queries by splitting them into two segments using a precomputed prefix sum array. |
| 2026-07-24 | Prefix Sum | 26090 | Counted valid continuous subsegments where both the length and the sum of the elements are prime numbers. Implemented an $O(\sqrt{N})$ prime checking function and efficiently calculated subsegment sums to prevent time limit exceeded (TLE). |
| 2026-07-27 | Prefix Sum | 16507 | Optimized 2D subgrid sum queries from O(R * C) to O(1) by precomputing a 2D prefix sum matrix. Applied the inclusion-exclusion principle to accurately extract the exact sum of the target area and compute the average brightness efficiently. |
