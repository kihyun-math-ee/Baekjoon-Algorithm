import sys
from collections import deque

# BOJ 1966: Printer Queue (Data Structure / Queue Simulation)
# Time Complexity: O(N^2) per test case (Due to scanning the queue for priorities)
#
# Engineering Notes:
# 1. Used collections.deque for O(1) rotation (popleft and append).
# 2. Leveraged `enumerate` to permanently bind the original index to its priority
#    level, creating a tuple: (original_index, priority).
# 3. Implemented `any()` as an inline scanner to check the remaining queue 
#    for strictly higher priorities before permitting a print execution.

T = int(sys.stdin.readline())

for _ in range(T):
    N, M = map(int, sys.stdin.readline().split())
    priorities = map(int, sys.stdin.readline().split())
    
    # Pack the priorities with their original index: [(0, p0), (1, p1), ...]
    queue = deque(enumerate(priorities))
    print_count = 0
    
    while True:
        # Pop the front document
        current_doc = queue.popleft()
        
        # Check if any document left in the queue has a higher priority
        if any(doc[1] > current_doc[1] for doc in queue):
            queue.append(current_doc) # Throw to the back
        else:
            # It is the highest priority! Print it.
            print_count += 1
            # Was this our target document?
            if current_doc[0] == M:
                print(print_count)
                break









        