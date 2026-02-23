import sys

# BOJ 2798: Blackjack (Brute Force)
# Time Complexity: O(N^3)
#
# Engineering Notes:
# 1. Implemented an exhaustive search (Brute Force) using 3 nested loops to simulate nC3 combinations.
# 2. Optimized the loop boundaries (N-2, N-1, N) to prevent out-of-bounds errors and redundant checks.
# 3. Converted the input array to integers immediately upon reading to prevent O(N^3) redundant type conversions during execution.
# 4. *Alternative Pythonic approach: itertools.combinations(cards, 3) can abstract this logic entirely.

N, M = map(int, sys.stdin.readline().split())
cards = list(map(int, sys.stdin.readline().split()))
Max_cards = 0

for i in range(0, N - 2):
    for j in range(i + 1, N - 1):
        for k in range(j + 1, N):
            current_sum = cards[i] + cards[j] + cards[k]
            if Max_cards <= current_sum <= M:
                Max_cards = current_sum

print(Max_cards)

