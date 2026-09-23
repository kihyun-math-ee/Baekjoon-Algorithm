# Binary Search

This folder contains 6 BOJ solution files. Dates are the earliest recorded study dates in the original Study Log.

## 📅 Study Log

| Date | Category | Problem | Key Learnings |
| :--- | :--- | :--- | :--- |
| 2026-08-13 | Binary Search | 1654 | Implemented Parametric Search (Binary Search) to find the maximum possible length of LAN cables. Configured the search space between 1 and the maximum existing cable length. Efficiently updated the optimal length (`result = mid`) when the generated number of cables met or exceeded the requirement (`S >= N`), systematically narrowing down the search range. |
| 2026-08-17 | Binary Search | 1939 | Implemented Parametric Search combined with Breadth-First Search (BFS) to determine the maximum transportable weight between two factories. The binary search efficiently narrows down the optimal weight within a maximum range of 1,000,000,000, while the BFS validates path connectivity by filtering edges that meet or exceed the target weight limit. |
| 2026-08-25 | Binary Search | 2512 | Implemented a parametric search algorithm to determine the optimal budget cap. Effectively utilized binary search logic to find the maximum possible threshold, dynamically updating the total allocated budget to strictly adhere to the given constraint. Achieved $\mathcal{O}(N \log(\text{max}))$ time complexity. |
| 2026-09-06 | Binary Search | 10425 | Precomputed the Fibonacci sequence to establish a search space. Implemented Binary Search to efficiently locate the exact index of extremely large Fibonacci numbers in $O(\log N)$ time. |
| 2026-09-07 | Binary Search | 2343 | Translated an optimization problem into a decision problem to find the minimum possible blueray size. Established precise boundary conditions (`low = max(L)`, `high = sum(L)`) and implemented an $O(N)$ sequential evaluation logic to validate the partition count within the $O(\log(\sum L))$ search space. |
| 2026-09-24 | Binary Search | 3896 | Precomputed primes up to 1,299,709 via the Sieve of Eratosthenes. Implemented a custom upper bound binary search to pinpoint bounding primes in $O(\log \pi(M))$ time per query, determining composite sequence intervals without redundant linear scans. |
