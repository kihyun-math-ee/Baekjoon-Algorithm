import sys
from collections import deque

# 1. Setup
N, K = map(int, sys.stdin.readline().split())
queue = deque(range(1, N + 1))  # Create deque: [1, 2, 3, ..., N]
result = []

# 2. The Universal Loop (Works for any size)
while queue:
    # ROTATE: Move K-1 people from Front to Back
    # This simulates "skipping" people in the circle
    # deque.rotate(-n) moves n items from left to right
    queue.rotate(-(K - 1))
    
    # KILL: Pop the person at the Front
    result.append(queue.popleft())

# 3. Formatting Output (Crucial for BOJ)
# BOJ requires "<1, 3, ...>" not "[1, 3, ...]"
print(f"<{', '.join(map(str, result))}>")
