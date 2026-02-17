import sys
from collections import deque

# [Track B] Queue Implementation using collections.deque
# Optimization: Replaced Python List with Deque (Double-Ended Queue)
# Result: 'pop' operation improved from O(N) to O(1).
class Queue:
    def __init__(self):
        # Time Complexity: O(1)
        # deque is implemented as a doubly linked list internally.
        self.queue = deque()

    def push(self, X):
        # Time Complexity: O(1)
        # Appending to the end of a deque is instant.
        self.queue.append(X)

    def pop(self):
        # [CRITICAL OPTIMIZATION] Time Complexity: O(1)
        # Reason: Unlike list.pop(0) which shifts all elements (O(N)),
        # deque.popleft() simply unlinks the first node. Zero shifting required.
        if not self.queue:
            return -1
        return self.queue.popleft()
    
    def size(self):
        # Time Complexity: O(1)
        return len(self.queue)
    
    def empty(self):
        # Time Complexity: O(1)
        return 1 if not self.queue else 0
    
    def front(self):
        # Time Complexity: O(1)
        # Accessing the first element [0] is direct.
        if not self.queue:
            return -1
        return self.queue[0]
    
    def back(self):
        # Time Complexity: O(1)
        # Accessing the last element [-1] is direct.
        if not self.queue:
            return -1
        return self.queue[-1]
    
    def check(self):
        # [Debug Tool] Time Complexity: O(N)
        # Reason: Casting deque to list requires iterating all N elements.
        # Use only for debugging, not inside high-performance loops.
        print(list(self.queue))

    def reverse(self):
        # [Feature] Time Complexity: O(N)
        # Reason: Must traverse and swap pointers for all N nodes.
        self.queue.reverse()
        print("Queue Reversed.")

    
if __name__ == "__main__":
    N = int(sys.stdin.readline())
    my_queue = Queue()
    
    for _ in range(N):
        line = sys.stdin.readline().split()
        command = line[0]
        
        if command == 'push':
            number = int(line[1])
            my_queue.push(number)

        elif command == 'pop':
            print(my_queue.pop())

        elif command == 'size':
            print(my_queue.size())

        elif command == 'empty':
            print(my_queue.empty())

        elif command == 'front':
            print(my_queue.front())

        elif command == 'back':
            print(my_queue.back())

        elif command == 'check':
            my_queue.check()

        elif command == 'reverse':
            my_queue.reverse()