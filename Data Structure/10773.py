import sys

class Stack:
    def __init__(self):
        # Initialize an empty list to act as our Stack (Ledger).
        self.stack = []

    def zero_pop(self, zero_input):
        # If the boss shouts "0", we erase the most recent mistake.
        if zero_input == 0:
            # .pop() removes the last item added (LIFO: Last-In, First-Out).
            self.stack.pop()
        else:
            # If it's a valid number, we write it down in the ledger.
            self.stack.append(zero_input)
        
        # Return current state of the stack (optional, but good practice).
        return self.stack
    
    def Sum_stack(self):
        # sum() is an optimized built-in function to calculate the total of the list.
        # Time Complexity: O(N), where N is the current size of the stack.
        print(sum(self.stack))

if __name__ == "__main__":
    # 1. Instantiate the Stack object.
    my_stack = Stack()
    
    # 2. Read K, which represents the total number of commands to follow.
    K = int(sys.stdin.readline())
    
    # 3. Loop exactly K times to process each command.
    for _ in range(K):
        N = int(sys.stdin.readline())
        my_stack.zero_pop(N)

    # 4. Print the final calculated sum of the remaining numbers.
    my_stack.Sum_stack()

    
