import sys

# BOJ 24313: Asymptotic Notation 1
# Time Complexity: O(1)
#
# Mathematical Proof of Big-O: O(n)
# Definition: f(n) <= c * n for all n >= n_0
# 
# 1. For the inequality to hold true to infinity, the slope 'c' must be 
#    greater than or equal to the slope 'a_1' (c >= a_1).
# 2. If the slope condition is met, we only need to verify that the inequality 
#    holds true at the starting point n_0.
# 3. Therefore, if f(n_0) <= c * n_0 AND c >= a_1, the condition is satisfied.

a_1, a_0 = map(int, sys.stdin.readline().split())
c = int(sys.stdin.readline())
n_0 = int(sys.stdin.readline())

if (a_1 * n_0 + a_0 <= c * n_0) and (c >= a_1):
    print(1)
else:
    print(0)