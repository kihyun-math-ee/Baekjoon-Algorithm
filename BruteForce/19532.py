import sys

# BOJ 19532: Mathematics - non-contact equation (Brute Force vs Math)
# Time Complexity: O(N^2) via Brute Force, O(1) via Linear Algebra
#
# Engineering Notes:
# 1. Pedagogical Intent (Brute Force): Implemented an exhaustive O(N^2) search 
#    checking all 4,000,000 possible coordinates in the range [-999, 999].
#    Utilized sys.exit(0) to halt execution immediately upon finding the target.
# 2. Mathematical Optimization (O(1)): The system guarantees a unique solution,
#    meaning the determinant (ae - bd) != 0. 
#    We can bypass the O(N^2) loops entirely using Cramer's Rule / Inverse Matrices:
#    x = (ce - bf) // (ae - bd)
#    y = (af - cd) // (ae - bd)

a, b, c, d, e, f = map(int, sys.stdin.readline().split())

# --- Method 1: The O(1) Mathematical Approach (Optimal) ---
# x = (e*c - b*f) // (a*e - b*d)
# y = (a*f - c*d) // (a*e - b*d)
# print(x, y)

# --- Method 2: The O(N^2) Brute Force Approach (Intended) ---
for x in range(-999, 1000):
    for y in range(-999, 1000):
        if (a*x + b*y == c) and (d*x + e*y == f):
            print(x, y)
            sys.exit(0)