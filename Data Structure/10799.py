import sys

class Stack_pipes:
    def __init__(self):
        # Initialize an empty list to act as our Stack for holding active pipes.
        self.stack = []
        # Initialize a counter to track the total pieces of cut iron.
        self.total_pieces = 0

    def pipes_count(self, p):
        # Time Complexity: O(N), where N is the length of the string 'p'.
        # We sweep through the string exactly once from left to right.
        for i in range(len(p)):
            
            # If we see an opening bracket, it could be a new pipe OR the start of a laser.
            # We temporarily assume it's a pipe and push it to the stack.
            if p[i] == '(':
                self.stack.append('(')

            # If we see a closing bracket, we must determine if it's a laser or a pipe ending.
            else:
                # Condition 1: It's a Laser '()'
                # If the immediately preceding character was '(', the laser fires!
                if p[i - 1] == '(':
                    # Remove the '(' we just added because it was a laser, not a pipe.
                    self.stack.pop()
                    # The laser cuts all currently active pipes in the stack.
                    # We add the exact number of active layers to our total pieces.
                    self.total_pieces += len(self.stack)
                
                # Condition 2: It's the end of an Iron Pipe ')'
                # If the preceding character was also ')', a pipe has physically finished.
                else:
                    # Remove the pipe from the active stack (it is no longer being cut).
                    self.stack.pop()
                    # The very tail end of the pipe drops off as exactly 1 piece of scrap iron.
                    self.total_pieces += 1

        # Print the final calculated total of all cut iron pieces.
        print(self.total_pieces)


if __name__ == '__main__':
    # 1. Instantiate the Stack_pipes object.
    my_pipes = Stack_pipes()
    
    # 2. Read the sequence of brackets and strip the hidden newline character.
    S = sys.stdin.readline().strip()
    
    # 3. Execute the O(N) sweep logic to count the cut pieces.
    my_pipes.pipes_count(S)
