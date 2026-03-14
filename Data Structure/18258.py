import sys
from collections import deque

# [Track B] Queue Implementation for Sequential Data (BOJ 18258)
# Optimization: Utilized collections.deque to achieve strictly O(1) time complexity for all FIFO (First-In-First-Out) operations.
# Result: O(N) overall execution, successfully bypassing the O(N^2) bottleneck of standard list pop(0).

# Initialize the double-ended queue
# Time Complexity: O(1)
my_queue = deque()

N = int(sys.stdin.readline())

# Time Complexity: O(N) where N is the number of commands
for _ in range(N):
    # [CRITICAL OPTIMIZATION] Variable-Length Input Parsing
    # Reason: The 'push' command has two elements ("push X"), but all others have one.
    # .split() safely creates a list so we can check the command type before looking for a second element.
    line = sys.stdin.readline().strip().split()
    
    # Command 1: Push X to the back of the queue
    if line[0] == 'push':
        # Time Complexity: O(1)
        # Note: Appending as a string saves CPU cycles since no math is performed on it.
        my_queue.append(line[1])
        
    # Command 2: Pop and print the front element
    elif line[0] == 'pop':
        # [CRITICAL GUARD] Prevent IndexError by checking if the queue exists
        # [CRITICAL OPTIMIZATION] popleft() is strictly O(1), whereas list.pop(0) is O(N)
        if my_queue:
            print(my_queue.popleft())
        else:
            print(-1)
            
    # Command 3: Print the size of the queue
    elif line[0] == 'size':
        # Time Complexity: O(1)
        print(len(my_queue))
        
    # Command 4: Check if the queue is empty
    elif line[0] == 'empty':
        # Time Complexity: O(1)
        if not my_queue:
            print(1)  # Empty
        else:
            print(0)  # Not empty
            
    # Command 5: Print the front element without popping
    elif line[0] == 'front':
        # [CRITICAL GUARD] Prevent IndexError
        # Time Complexity: O(1)
        if not my_queue:
            print(-1)
        else:
            print(my_queue[0])
            
    # Command 6: Print the back element without popping
    elif line[0] == 'back':
        # [CRITICAL GUARD] Prevent IndexError
        # Time Complexity: O(1)
        if not my_queue:
            print(-1)
        else:
            print(my_queue[-1])