"""
BOJ 11866: Josephus Problem 0
Data Structure: collections.deque
Time Complexity: O(N * K) overall, O(K) per rotation
Logic:
- Uses a deque to represent the circular table.
- rotate(-(K-1)) efficiently shifts the queue so the target person lands at index 0.
- popleft() removes them in O(1) time.
- Uses string join formatting to exactly match BOJ's strict output constraints.
"""
import sys
from collections import deque

N, K = map(int, sys.stdin.readline().split())
sequence = []
my_deque = deque(range(1, N + 1))

for _ in range(N):
    # Shift the queue left so the target person is at the very front
    my_deque.rotate(-(K-1))
    # Remove the target person in O(1) time and record them
    sequence.append(my_deque.popleft())

# BOJ strict formatting: <1, 2, 3> without extra padding
print(f"<{', '.join(map(str, sequence))}>")