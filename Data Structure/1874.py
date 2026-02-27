import sys

class Stacksequence:
    def __init__(self):
        self.stack = []
        self.result = []      # Save answers here instead of printing
        self.current = 1      # The numbers 1, 2, 3, 4... we push into the stack
        self.is_possible = True

    def push_pop(self, target_num):
        # RULE 1: Catch up to the target_num
        # If our current number is 1, and the target_num is 4...
        # We must push 1, 2, 3, 4 into the stack.
        while target_num >= self.current:
            self.stack.append(self.current)
            self.result.append("+")
            self.current += 1

        # RULE 2: Now that we caught up, the top of the stack SHOULD be target_num
        # (Added self.stack check to prevent IndexError on empty lists)
        if self.stack and (self.stack[-1] == target_num):
            self.stack.pop()
            self.result.append("-")

        # RULE 3: If the top of the stack is NOT target_num, it's impossible
        else:
            self.is_possible = False

    def print_result(self):
        # FINAL OUTPUT
        if self.is_possible == False:
            print("NO")
        else:
            # Print everything in the result list cleanly
            print("\n".join(self.result))


if __name__ == "__main__":
    my_stacksequence = Stacksequence()
    n = int(sys.stdin.readline())
    
    for _ in range(n):
        current_target = int(sys.stdin.readline()) # Just get the next number we need
        my_stacksequence.push_pop(current_target)
        
        # Early Exit: If it becomes impossible, break the loop immediately
        if my_stacksequence.is_possible == False:
            break

    my_stacksequence.print_result()

