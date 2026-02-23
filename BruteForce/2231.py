import sys

# BOJ 2231: Decomposition (Brute Force / Exhaustive Search)
# Time Complexity: Optimized from O(N) to near O(1) using mathematical bounds.
#
# Engineering Notes:
# 1. Base logic utilizes Exhaustive Search to find the smallest generator.
# 2. Mathematical Optimization: A generator M can never be smaller than N - (number of digits * 9).
#    By starting the search at this calculated floor, we bypass hundreds of thousands
#    of unnecessary iterations, drastically dropping the execution time.
# 3. Utilized Python's `sum(map(int, str(i)))` for rapid integer-to-digit summation.
# 4. Implemented Python's native `for-else` structure to cleanly handle the 
#    "no generator found" edge case (printing 0) without needing infinity flags.

N_str = sys.stdin.readline().strip()
N = int(N_str)

# Calculate the mathematical floor for the brute force search
# (e.g., if N=216, max digit sum is 9+9+9=27. We only need to search from 216-27 = 189)
start_point = max(1, N - (len(N_str) * 9))

for i in range(start_point, N):
    # Calculate decomposition sum: the number itself + the sum of its digits
    decomposition_sum = i + sum(map(int, str(i)))
    
    # The first match is mathematically guaranteed to be the minimum
    if decomposition_sum == N:
        print(i)
        break
else:
    # This block executes ONLY if the loop finishes without hitting the 'break'
    print(0)



    

