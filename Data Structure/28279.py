"""
BOJ 28279: Deque 2
Data Structure: collections.deque (OOP State Machine)
Time Complexity: O(1) for all 8 operations
Logic:
- Engineered as an Object-Oriented 'Machine' class to safely encapsulate state.
- Uses sys.stdin.readline().split() keeping inputs as strings to bypass int() conversion CPU cycles.
- Deque provides guaranteed O(1) performance for appending and popping on both ends.
"""
import sys
from collections import deque

class Machine:
    def __init__(self):
        # Initialize the core engine
        self.double_ended_queue = deque()

    def Action(self, sentence):
        # Command 1: Insert at front
        if sentence[0] == '1':
            self.double_ended_queue.appendleft(sentence[1])
        # Command 2: Insert at rear
        elif sentence[0] == '2':
            self.double_ended_queue.append(sentence[1])
        # Command 3: Pop front
        elif sentence[0] == '3':
            if self.double_ended_queue:
                print(self.double_ended_queue.popleft())
            else:
                print(-1)
        # Command 4: Pop rear
        elif sentence[0] == '4':
            if self.double_ended_queue:
                print(self.double_ended_queue.pop())
            else:
                print(-1)
        # Command 5: Size
        elif sentence[0] == '5':
            print(len(self.double_ended_queue)) 
        # Command 6: Is empty?
        elif sentence[0] == '6':
            if not self.double_ended_queue:
                print(1)
            else:
                print(0)
        # Command 7: Peek front
        elif sentence[0] == '7':
            if self.double_ended_queue:
                print(self.double_ended_queue[0])
            else:
                print(-1)
        # Command 8: Peek rear
        elif sentence[0] == '8':
            if self.double_ended_queue:
                print(self.double_ended_queue[-1])
            else:
                print(-1)

if __name__ == '__main__':
    # Instantiate the state machine
    my_deque = Machine()
    N = int(sys.stdin.readline())
    
    for _ in range(N):
        line = sys.stdin.readline().strip().split()
        my_deque.Action(line)