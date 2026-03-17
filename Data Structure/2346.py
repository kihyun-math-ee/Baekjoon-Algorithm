"""
BOJ 2346: Balloon Popping
Data Structure: collections.deque
Time Complexity: O(N * K) overall (where K is the rotation distance)
Logic:
- Simulates a circular sequence of popping balloons using a deque.
- Maps the deque's balloon ID back to the original static array `num_list` to find the rotation value.
- Implements "Ghost Step" math: Subtracts 1 from positive movements to account for the free rightward shift caused by popleft().
- Note: Slated for an `enumerate` refactor warm-up tomorrow!
"""
import sys
from collections import deque

N = int(sys.stdin.readline())
num_list = list(map(int, sys.stdin.readline().split()))

# Store only the balloon IDs (1 to N) in the deque
balloon_deque = deque(range(1, N + 1))
result = []
cnt = 0

# Pop the first balloon outside the loop to initialize the state
result.append(balloon_deque.popleft())

# Calculate the initial rotation, accounting for the first ghost step if positive
if num_list[0] > 0:
    i = num_list[0] - 1
else:
    i = num_list[0]

while cnt != N - 1:
    # Rotate the deque. Negative 'i' correctly maps to moving forward in the circle
    balloon_deque.rotate(-i)

    # Look up the next balloon's paper value and calculate the next rotation
    if num_list[balloon_deque[0] - 1] > 0:
        i = num_list[balloon_deque[0] - 1] - 1
    else:
        i = num_list[balloon_deque[0] - 1]

    # Pop the current balloon and record its ID
    result.append(balloon_deque.popleft())
    cnt += 1

# Unpack the list to print as space-separated integers for BOJ
print(*result)