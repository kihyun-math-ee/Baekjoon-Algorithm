import sys

# Optimization: Custom Object-Oriented Architecture with separated logic blocks.
# Result: O(N) overall execution with strict O(1) time complexity per stack operation.
class Stack:
    def __init__(self):
        # Time Complexity: O(1)
        # Initialize the global state for the stack object.
        self.stack = []

    def Machine(self, command, target):
        # Command 1: Push X onto the stack
        # Time Complexity: O(1) amortized
        if command == 1:
            self.stack.append(target)
        
    def Machine_2(self, command_2):
        # Command 2: Pop and print the top element
        if command_2 == 2:
            # [CRITICAL GUARD] Prevent IndexError by checking if stack is empty
            # Time Complexity: O(1)
            if self.stack:
                print(self.stack.pop())
            else:
                print(-1)
        
        # Command 3: Print the number of elements in the stack
        elif command_2 == 3:
            # Time Complexity: O(1)
            print(len(self.stack))
        
        # Command 4: Check if the stack is empty
        elif command_2 == 4:
            # Time Complexity: O(1)
            if self.stack:
                print(0)  # Not empty
            else:
                print(1)  # Empty
        
        # Command 5: Print the top element without popping
        elif command_2 == 5:
            # [CRITICAL GUARD] Prevent IndexError when looking at the top element
            # Time Complexity: O(1)
            if self.stack:
                print(self.stack[-1])
            else:
                print(-1)

if __name__=='__main__':
    my_stack = Stack()
    N = int(sys.stdin.readline())
    
    # Time Complexity: O(N) where N is the number of commands
    for _ in range(N):
        # [CRITICAL OPTIMIZATION] Variable-Length Input Parsing
        # Reason: Command 1 has two integers ("1 X"), but others have only one ("2").
        # Using .split() creates a list, allowing us to safely check the command 
        # type before trying to access a second index that might not exist.
        line = sys.stdin.readline().split()
        given_command = int(line[0])
        
        if given_command == 1:
            number = int(line[1])
            my_stack.Machine(given_command, number)
        
        else:
            my_stack.Machine_2(given_command)
        
        
        