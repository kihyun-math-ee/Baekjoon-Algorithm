import sys

class Stack:
    def __init__(self):
        # Initialize an empty list to act as the stack
        # This will store opening parentheses '(' waiting for a match
        self.stack = []

    def push_pop(self, text):
        """
        Process the input string.
        Returns: 
            False if the string is invalid immediately (e.g., pop from empty).
            True if the string processing finished without immediate errors.
        """
        for x in text:
            if x == '(':
                # If we see an Opening Parenthesis, PUSH it.
                # It needs a closing partner later.
                self.stack.append(x)
                
            elif x == ')':
                # If we see a Closing Parenthesis, we try to POP.
                
                # EDGE CASE: Stack is empty but we found a ')'
                if len(self.stack) == 0:
                    print('NO')   # Immediate failure
                    return False  # <--- CRITICAL: Signal 'Failure' to the main loop
                
                # Normal Case: Stack has items, so we pop the matching '('
                elif len(self.stack) > 0:
                    self.stack.pop()
                    
        # If we loop through the whole string without crashing, signal 'Success' (so far)
        return True

    def check(self):
        """
        Final check after processing the entire string.
        """
        # If the stack is empty, every '(' found its matching ')'. Success!
        if len(self.stack) == 0:
            print("YES")
            
        # If the stack still has items (e.g., '((('), it's invalid.
        elif len(self.stack) > 0:
            print("NO")

if __name__ == "__main__":
    # Read the number of test cases
    N = int(sys.stdin.readline())
    
    for _ in range(N):
        # 1. Create a NEW Stack instance for every test case.
        # This ensures we don't carry over garbage data from the previous case.
        my_stack = Stack()
        
        # Read input strip() removes the hidden '\n' newline character
        text = sys.stdin.readline().strip()
        
        # 2. Logic Flow:
        # Run push_pop first. If it returns False (Invalid), STOP.
        # Only run check() if push_pop returns True.
        if my_stack.push_pop(text) == True:
            my_stack.check()