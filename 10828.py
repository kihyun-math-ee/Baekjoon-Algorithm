import sys

# [Track B] Stack Implementation with Python List
# Time Complexity Analysis: Amortized O(1) for push
class Stack:
    def __init__(self):
        self.stack = []

    def push(self, X):
        # Time Complexity: Amortized O(1)
        # Reason: Python lists are dynamic arrays. Resizing (copying) happens rarely (when full).
        # Most operations are simple assignments O(1), making the average cost O(1).
        self.stack.append(X)
    
    def pop(self):
        # Time Complexity: O(1)
        # Reason: Removing the last element doesn't require shifting other elements.
        if len(self.stack) == 0:
            return -1
        return self.stack.pop()

    def size(self):
        # Time Complexity: O(1)
        # Reason: Python lists store their length in a generic struct variable (ob_size).
        return len(self.stack)

    def empty(self):
        # Time Complexity: O(1)
        if len(self.stack) == 0:
            return 1
        else:
            return 0

    def top(self):
        # Time Complexity: O(1)
        # Reason: Direct index access is constant time.
        if len(self.stack) == 0:
            return -1
        return self.stack[-1]

if __name__ == "__main__":
    N = int(sys.stdin.readline())
    my_stack = Stack()  # 인스턴스 생성
    
    for _ in range(N):
        command = sys.stdin.readline().split()
        cmd_type = command[0]
        
        if cmd_type == 'push':
            # push 명령은 뒤에 숫자가 따라옴
            my_stack.push(int(command[1]))
        
        elif cmd_type == 'pop':
            print(my_stack.pop())
        
        elif cmd_type == 'size':
            print(my_stack.size())

        elif cmd_type == 'empty':
            print(my_stack.empty())

        elif cmd_type == 'top':
            print(my_stack.top())