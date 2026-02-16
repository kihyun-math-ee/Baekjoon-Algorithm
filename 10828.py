import sys

# [Track B] Extended Stack Implementation with Python List
# Features: Standard LIFO + Debugging (Check) + Manipulation (Reverse)
class Stack:
    def __init__(self):
        # Initialization
        # Time Complexity: O(1)
        self.stack = []

    def check(self):
        # [Experiment] Debugging Tool
        # Time Complexity: O(N) 
        # Reason: Must iterate through all N elements to print them.
        print(self.stack)

    def push(self, X):
        # Time Complexity: Amortized O(1)
        # Reason: Python lists are dynamic arrays. Resizing happens rarely.
        # Most appends are simple assignments at the end.
        self.stack.append(X)

    def pop(self):
        # Time Complexity: O(1)
        # Reason: Removing the last element is instant. No shifting required.
        if len(self.stack) == 0:
            print(-1)
        else:    
            print(self.stack.pop())

    def size(self):
        # Time Complexity: O(1)
        # Reason: Python stores the list length in a struct variable (ob_size).
        # It does not count elements every time.
        print(len(self.stack))

    def empty(self):
        # Time Complexity: O(1)
        if len(self.stack) == 0:
            print(1)
        else:
            print(0)

    def top(self):
        # Time Complexity: O(1)
        # Reason: Direct index access [-1] is constant time.
        if len(self.stack) == 0:
            print(-1)
        else:
            print(self.stack[-1])

    def reverse(self):
        # [Experiment] Reverse the Stack order
        # Time Complexity: O(N)
        # Reason: Must swap N/2 pairs of elements in memory.
        # This is significantly more expensive than push/pop.
        self.stack.reverse()
        print("Stack Reversed.")

# --- Main Execution ---
if __name__ == "__main__":
    N = int(sys.stdin.readline())
    my_stack = Stack()
    
    for _ in range(N):
        line = sys.stdin.readline().split()
        command = line[0]

        if command == 'push':
            number = int(line[1])
            my_stack.push(number)

        elif command == 'pop':
            my_stack.pop()

        elif command == 'size':
            my_stack.size()

        elif command == 'empty':
            my_stack.empty()

        elif command == 'top':
            my_stack.top()

        elif command == 'check':
            my_stack.check()

        elif command == 'reverse':
            my_stack.reverse()