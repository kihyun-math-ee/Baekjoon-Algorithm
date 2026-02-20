import sys
from collections import deque

# 1. Input
N = int(sys.stdin.readline())

# 2. Build the Deque instantly (1 to N)
my_deque = deque(range(1, N + 1))

# 3. The Simulation Loop
while len(my_deque) > 1:
    my_deque.popleft()                   # Throw away the top card
    my_deque.append(my_deque.popleft())  # Take the new top card and put it on the bottom

# 4. Output the last remaining card
print(my_deque[0])


    