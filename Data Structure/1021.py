import sys
from collections import deque

# [Track B] Deque Implementation for Minimum Rotation Cost (BOJ 1021)
# Optimization: Utilized double-ended queue (Deque) for O(1) bidirectional rotations 
# and dynamic midpoint calculation to guarantee the shortest rotation path.
# Result: O(N * M) overall execution with minimized rotational cost.

# Time Complexity: O(N) where N is the total size of the queue
N, M = map(int, sys.stdin.readline().split())

# Initialize the deque with numbers 1 through N
my_deque = deque(range(1, N + 1))
target_list = list(map(int, sys.stdin.readline().split()))
cost_min = 0

for target in target_list:
    # Time Complexity: O(N) to find the index of the target in the current deque
    target_index = my_deque.index(target)

    # [CRITICAL OPTIMIZATION] Dynamic Midpoint Calculation
    # Reason: We must dynamically recalculate the halfway point because the length 
    # of the deque shrinks every time we pop an element.
    halfway = len(my_deque) // 2

    # If the target is in the front half, it is cheaper to rotate Left (Command 2)
    if target_index <= halfway:
        # Time Complexity: O(K) where K is the number of rotations
        # rotate(-x) shifts the deque to the left
        my_deque.rotate(-target_index)
        cost_min += target_index
        
    # If the target is in the back half, it is cheaper to rotate Right (Command 3)
    else:
        # Calculate exactly how many right spins are needed to bring it to index 0
        spins_needed = len(my_deque) - target_index
        # rotate(x) shifts the deque to the right
        my_deque.rotate(spins_needed)
        cost_min += spins_needed

    # Command 1: Extract the element once it is at the front (index 0)
    # Time Complexity: O(1)
    my_deque.popleft()

print(cost_min)
