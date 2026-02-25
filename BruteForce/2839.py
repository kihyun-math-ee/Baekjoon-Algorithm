import sys

# BOJ 2839: Sugar Delivery
# Category: Math / Greedy / Brute Force
# Logic: Try minimal 3kg bags to maximize 5kg bags.

N = int(sys.stdin.readline())
ans = -1

# Optimization: We only need to check 3kg bags until 3*i exceeds N
for i in range((N // 3) + 1):
    remaining_weight = N - (3 * i)
    
    if remaining_weight % 5 == 0:
        ans = i + (remaining_weight // 5)
        print(ans)
        break # Found the optimal solution (min 3kg used)
else:
    # This else executes ONLY if the loop finishes without breaking
    print(-1)
