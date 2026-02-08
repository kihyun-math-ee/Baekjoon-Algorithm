import sys

# [Track B] Queue Implementation with Python List
# Time Complexity Analysis: pop(0) is O(N)
class Queue:
    def __init__(self):
        self.queue = []

    def push(self, X):
        # Time Complexity: Amortized O(1)
        self.queue.append(X)
    
    def pop(self):
        # [Critical] Time Complexity: O(N)
        # Reason: Removing the first element (index 0) requires shifting 
        # all remaining N-1 elements one step forward to fill the gap.
        if not self.queue:
            return -1
        return self.queue.pop(0)

    def size(self):
        # Time Complexity: O(1)
        return len(self.queue)

    def empty(self):
        # Time Complexity: O(1)
        return 1 if not self.queue else 0

    def front(self):
        # Time Complexity: O(1)
        if not self.queue:
            return -1
        return self.queue[0]

    def back(self):
        # Time Complexity: O(1)
        if not self.queue:
            return -1
        return self.queue[-1]

if __name__ == "__main__":
    N = int(sys.stdin.readline())
    my_queue = Queue()
    
    for _ in range(N):
        command = sys.stdin.readline().split()
        cmd_type = command[0]
        
        if cmd_type == 'push':
            my_queue.push(int(command[1]))
        elif cmd_type == 'pop':
            print(my_queue.pop())
        elif cmd_type == 'size':
            print(my_queue.size())
        elif cmd_type == 'empty':
            print(my_queue.empty())
        elif cmd_type == 'front':
            print(my_queue.front())
        elif cmd_type == 'back':
            print(my_queue.back())