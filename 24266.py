import sys

# BOJ 24266: Algorithm Execution Time 5
# Time Complexity: O(N^3)
#
# Analysis of Pseudocode:
# MenOfPassion(A[], n) {
#     sum <- 0;
#     for i <- 1 to n
#         for j <- 1 to n
#             for k <- 1 to n
#                 sum <- sum + A[i] × A[j] × A[k]; # Code 1
#     return sum;
# }
#
# 1. The outermost loop 'i' runs 'n' times.
# 2. The middle loop 'j' runs 'n' times for each 'i'.
# 3. The innermost loop 'k' runs 'n' times for each 'j'.
# 4. Total executions: n * n * n = n^3.
# 5. Because it runs in cubic time O(N^3), the highest polynomial degree is 3.

n = int(sys.stdin.readline())
print(n**3)
print(3)