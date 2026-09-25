# Dynamic Programming

This folder contains 13 BOJ solution files. Existing dates follow the original Study Log; new entries use the archive date.

## 📅 Study Log

| Date | Category | Problem | Key Learnings |
| :--- | :--- | :--- | :--- |
| 2026-07-01 | Dynamic Programming | 9461 | Precomputed the Padovan sequence array up to N=100 using a bottom-up DP approach (f[i] = f[i-1] + f[i-5]) to handle multiple test cases in O(1) time per query. |
| 2026-07-02 | Dynamic Programming | 1149 | Implemented a 2D state DP approach to minimize cumulative cost, ensuring adjacent houses do not share the same color by selecting the minimum from the other two previous color states. |
| 2026-07-03 | Dynamic Programming | 1932 | Implemented a 2D DP approach to calculate the maximum cumulative sum path in an integer triangle, efficiently handling edge walls and inner diagonal paths. |
| 2026-07-04 | Dynamic Programming | 2156 | Implemented a 1D DP state transition to maximize the sum of wine volumes while strictly preventing three consecutive selections. |
| 2026-07-05 | Dynamic Programming | 2579 | Implemented a 1D DP state transition to maximize the score of climbing stairs while strictly preventing three consecutive steps. |
| 2026-07-10 | Dynamic Programming | 2705 | Solved recursive palindrome partitions by precomputing all valid combinations up to N=10000 to process each query in O(1) time. |
| 2026-07-12 | Dynamic Programming | 1463 | Solved the minimum operations problem using a bottom-up dynamic programming approach, checking divisibility by 2 and 3 to compute optimal subproblems in O(N) time. |
| 2026-07-14 | Dynamic Programming | 1699 | Solved the sum of squares problem using a bottom-up DP approach. Optimized the inner loop transition by only iterating through perfect squares up to the square root of the current number ($O(N\sqrt{N})$). |
| 2026-07-15 | Dynamic Programming | 1788 | Solved the extended Fibonacci sequence problem. Precomputed values up to 1,000,000 using bottom-up DP with modulo 1,000,000,000 to prevent memory/time overhead. Efficiently processed negative inputs in O(1) time by applying the mathematical property of Fibonacci numbers depending on whether the negative index is even or odd. |
| 2026-07-16 | Dynamic Programming | 1912 | Solved the maximum subarray sum problem using Dynamic Programming (Kadane's Algorithm). Efficiently determined whether to extend the previous contiguous sum or start a new subarray at each step using the recurrence relation `max(dp[i - 1] + L[i], L[i])`. Optimized time complexity to O(N) by calculating the maximum sum in a single pass. |
| 2026-07-25 | Dynamic Programming | 24416 | Compared the execution counts of recursion and dynamic programming (tabulation) approaches. Demonstrated how DP drastically reduces redundant calculations and optimizes time complexity from $O(2^N)$ to $O(N)$. |
| 2026-08-27 | Dynamic Programming | 2670 | Implemented an $O(N)$ Dynamic Programming solution to find the maximum contiguous product in an array of floats. Applied a state transition logic to track local maximums by comparing the current element with the product of the previous maximum and the current element. |
| 2026-09-26 | Dynamic Programming | 11053 | Used an O(N^2) Dynamic Programming approach to find the length of the Longest Increasing Subsequence. For each element, extended the best earlier subsequence ending at a strictly smaller value and returned the maximum DP state. |
