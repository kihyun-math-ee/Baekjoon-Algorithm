import sys

# [Track B] Deep Dive: Deque (Double-Ended Queue) Implementation
# -------------------------------------------------------------
# Analysis of Python List as a Deque:
# 1. Access/Append at End (Back): O(1)
#    - Python lists are dynamic arrays. Adding/removing from the end is instant.
# 2. Access/Insert at Start (Front): O(N)
#    - CRITICAL: Inserting or popping at index 0 requires shifting ALL elements 
#      in memory to new addresses. This is inefficient for large N.
#
# * Architectural Note:
#   In a real production environment, we use 'from collections import deque' 
#   which is implemented as a Doubly Linked List (O(1) for both ends).
# -------------------------------------------------------------

class Deque:
    def __init__(self):
        # Initialize an empty list to act as the deque container
        self.deque = []

    def push_front(self, X):
        # [Critical] Time Complexity: O(N)
        # Reason: All existing elements must shift right by 1 to make space at index 0.
        self.deque.insert(0, X)
    
    def push_back(self, X):
        # Time Complexity: O(1)
        # Reason: Simply adds to the available memory slot at the end.
        self.deque.append(X)
    
    def pop_front(self):
        # [Critical] Time Complexity: O(N)
        # Reason: After removing index 0, all remaining elements must shift left by 1.
        if not self.deque: 
            return -1
        return self.deque.pop(0)

    def pop_back(self):
        # Time Complexity: O(1)
        # Reason: Simply decrements the list size pointer. No shifting needed.
        if not self.deque: 
            return -1
        return self.deque.pop()
    
    def size(self):
        # Time Complexity: O(1) -> Length is stored as a variable in Python lists
        return len(self.deque)
    
    def empty(self):
        # Check if length is 0. Returns 1 (True) or 0 (False)
        return 1 if not self.deque else 0
    
    def front(self):
        # Return the first element without removing it
        return self.deque[0] if self.deque else -1
    
    def back(self):
        # Return the last element without removing it
        return self.deque[-1] if self.deque else -1
    
if __name__ == "__main__":
    # Use sys.stdin.readline for fast I/O
    N = int(sys.stdin.readline())
    my_deque = Deque()

    for _ in range(N):
        command = sys.stdin.readline().split()
        cmd_type = command[0]

        if cmd_type == 'push_front':
            my_deque.push_front(int(command[1]))
        
        elif cmd_type == 'push_back':
            my_deque.push_back(int(command[1]))

        elif cmd_type == 'pop_front':
            print(my_deque.pop_front())

        elif cmd_type == 'pop_back':
            print(my_deque.pop_back())

        elif cmd_type == 'size':
            print(my_deque.size())

        elif cmd_type == 'empty':
            print(my_deque.empty())

        elif cmd_type == 'front':
            print(my_deque.front())

        elif cmd_type == 'back':
            print(my_deque.back())