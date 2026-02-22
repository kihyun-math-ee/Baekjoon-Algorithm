import sys

# BOJ 24265: Algorithm Execution Time 4
# Time Complexity: O(N^2)
#
# Analysis of Pseudocode:
# MenOfPassion(A[], n) {
#     sum <- 0;
#     for i <- 1 to n - 1
#         for j <- i + 1 to n
#             sum <- sum + A[i] × A[j]; # Code 1
#     return sum;
# }
#
# 1. The outer loop runs from 1 to n - 1.
# 2. The inner loop runs from i + 1 to n. 
# 3. This creates an arithmetic progression of executions: (n-1) + (n-2) + ... + 1.
# 4. The total sum of executions is exactly n(n-1)/2.
# 5. Because the dominant term is n^2, it runs in quadratic time O(N^2).

n = int(sys.stdin.readline())
print((n * (n - 1)) // 2)
print(2)