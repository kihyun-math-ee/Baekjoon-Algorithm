import sys

# BOJ 24264: Algorithm Execution Time 3
# Time Complexity: O(N^2)
#
# Analysis of Pseudocode:
# MenOfPassion(A[], n) {
#     sum <- 0;
#     for i <- 1 to n
#         for j <- 1 to n
#             sum <- sum + A[i] × A[j]; # Code 1
#     return sum;
# }
#
# 1. The outer loop executes 'n' times.
# 2. For every iteration of the outer loop, the inner loop executes 'n' times.
# 3. Therefore, the core logic executes exactly n * n (n^2) times.
# 4. Because it runs in quadratic time O(N^2), the highest polynomial degree is 2.

n = int(sys.stdin.readline())
print(n**2)
print(2)