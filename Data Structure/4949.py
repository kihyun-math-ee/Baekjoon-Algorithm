import sys

# [Track B] Stack Implementation for Multi-Bracket Validation
# Optimization: Utilized LIFO (Last-In-First-Out) architecture to balance nested structures.
# Result: O(N) single-pass validation with O(1) matching operations.
class Pair_Stack:
    def __init__(self):
        # Time Complexity: O(1)
        # Initialize the global state for the stack object.
        self.Stack = []
        self.is_symmetric = True

    def push_pop(self, X):
        # [CRITICAL OPTIMIZATION] Memory State Reset
        # Reason: Since we use the same object for multiple sentences, we MUST wipe the memory
        # clean at the START of every new sentence. If we only wipe it at the end, 
        # a 'break' command might skip the reset and corrupt the next sentence.
        self.Stack = []
        self.is_symmetric = True

        # Time Complexity: O(N) where N is the length of the sentence
        # We iterate through the string exactly once.
        for x in X:
            if x == '(':
                # Time Complexity: O(1)
                self.Stack.append('(')
            elif x == ')':
                # [CRITICAL GUARD] Prevent IndexError
                # Time Complexity: O(1)
                if not self.Stack:
                    self.is_symmetric = False
                    break
                elif self.Stack[-1] == '(':
                    self.Stack.pop()
                else:
                    self.is_symmetric = False
                    break
            
            elif x == '[':
                # Time Complexity: O(1)
                self.Stack.append('[')
            elif x == ']':
                # [CRITICAL GUARD] Prevent IndexError
                # Time Complexity: O(1)
                if not self.Stack:
                    self.is_symmetric = False
                    break
                elif self.Stack[-1] == '[':
                    self.Stack.pop()
                else:
                    self.is_symmetric = False
                    break

        # Final Validation: If the stack isn't empty after the loop, brackets were left unclosed.
        if self.Stack:
            self.is_symmetric = False

        if self.is_symmetric == True:
            print('yes')
        else:
            print('no')

if __name__ == '__main__':
    my_pair_stack = Pair_Stack()
    
    while True:
        # [CRITICAL OPTIMIZATION] rstrip('\n') instead of strip()
        # Reason: The problem explicitly states input is terminated by a single period ('.').
        # If the input is " .", using .strip() removes the space, making it ".",
        # which accidentally triggers the exit condition and crashes the program.
        given_sentence = sys.stdin.readline().rstrip('\n')
        
        if given_sentence == '.':
            sys.exit(0)
        else:
            my_pair_stack.push_pop(given_sentence)
