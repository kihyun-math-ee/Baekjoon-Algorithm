import sys

# BOJ 24263: Algorithm Execution Time 2
# Time Complexity: O(N)
#
# Analysis of Pseudocode:
# MenOfPassion(A[], n) {
#     sum <- 0;
#     for i <- 1 to n
#         sum <- sum + A[i]; # Code 1
#     return sum;
# }
#
# 1. The loop iterates from 1 to n.
# 2. Therefore, the core logic executes exactly 'n' times.
# 3. Because it runs in linear time O(N), the highest polynomial degree (n^1) is 1.

n = int(sys.stdin.readline())
print(n)
print(1)