"""
BOJ 24511: queuestack
Data Structure: collections.deque
Time Complexity: O(N + M)
Logic:
- Mathematical realization: Stacks (LIFO) in a 1-in/1-out system instantly pass the element through. They can be completely ignored.
- Uses list comprehension and zip() to filter out only the Queues (type 0) in O(N) time.
- Uses appendleft() and pop() on a deque to simulate the entire M sequence in strict O(M) time.
"""
import sys
from collections import deque

N = int(sys.stdin.readline())
A = list(map(int, sys.stdin.readline().split()))
B = list(map(int, sys.stdin.readline().split()))
M = int(sys.stdin.readline())
C = list(map(int, sys.stdin.readline().split()))

# Filter out stacks. Keep only the values from B where the corresponding type in A is 0 (Queue)
d = [val for val, typ in zip(B, A) if typ == 0]
target = 0
zero_result = deque(d)
result = []

for i in range(M):
    # Insert the new element at the front of the queue system in O(1) time
    zero_result.appendleft(C[i])
    # The element pushed out the back is our result
    result.append(zero_result.pop())

# Unpack the list to print as space-separated integers for BOJ
print(*result)