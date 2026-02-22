import sys

# BOJ 24267: Algorithm Execution Time 6
# Time Complexity: O(N^3)
#
# Analysis of Pseudocode:
# MenOfPassion(A[], n) {
#     sum <- 0;
#     for i <- 1 to n - 2
#         for j <- i + 1 to n - 1
#             for k <- j + 1 to n
#                 sum <- sum + A[i] × A[j] × A[k]; # Code 1
#     return sum;
# }
#
# 1. The three nested loops strictly enforce the condition i < j < k.
# 2. This is mathematically equivalent to choosing 3 distinct numbers from a set of n numbers (Combination nC3).
# 3. The formula for nC3 is n(n-1)(n-2) / 6.
# 4. Because the dominant term is n^3, it runs in cubic time O(N^3).

n = int(sys.stdin.readline())
print(((n-2)*(n-1)*(n))//6)
print(3)