import sys

# [Track B] Persistent Stack (Undo History Stack) Implementation
# Features: Standard LIFO + State Rollback (Undo) via History Logging
class Persistent_Stack:
    def __init__(self):
        # Initialization
        # Time Complexity: O(1)
        # Reason: Assigning empty lists takes constant time.
        self.L = []
        self.log = []
        self.tmp = []

    def instruction(self, X):
        if X[0] == 1:
            # [Command 1] Push
            # Time Complexity: Amortized O(1)
            # Reason: Python lists dynamically resize. Appending to L and log is standard O(1).
            self.L.append(X[1])
            self.log.append(1)
            
        elif X[0] == 2:
            # [Command 2] Pop
            # Time Complexity: O(1)
            # Reason: Popping the last element from L and appending it to tmp takes constant time.
            if self.L:
                self.tmp.append(self.L.pop())
                self.log.append(2)

        elif X[0] == 3:
            # [Command 3] Undo (Rollback)
            # Time Complexity: Amortized O(1)
            # Reason: Although there is a loop, each recorded action in `log` is popped exactly once globally. 
            # Over the entire execution, the total number of undo operations cannot exceed the total number of push/pop operations.
            for i in range(1, X[1] + 1):
                if not self.log:
                    break
                else:
                    if self.log[-1] == 1:
                        # Undo a Push: Remove the element from L
                        self.L.pop()
                        self.log.pop()
                    elif self.log[-1] == 2:
                        # Undo a Pop: Restore the element from tmp back to L
                        self.L.append(self.tmp.pop())
                        self.log.pop()

        elif X[0] == 4:
            # [Command 4] Size
            # Time Complexity: O(1)
            # Reason: Python stores the list length internally. len() does not count elements.
            print(len(self.L))

        elif X[0] == 5:
            # [Command 5] Top
            # Time Complexity: O(1)
            # Reason: Direct index access [-1] operates in constant memory time.
            if not self.L:
                print(-1)
            else:
                print(self.L[-1])

# --- Main Execution ---
if __name__ == "__main__":
    N = int(sys.stdin.readline())
    my_persistent_stack = Persistent_Stack()

    for _ in range(N):
        target = list(map(int, sys.stdin.readline().split()))
        my_persistent_stack.instruction(target)