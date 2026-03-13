import sys

# [Track B] Stack Implementation for State Machine Simulation (BOJ 12789)
# Optimization: Utilized a reversed array for O(1) pops and a strict 4-rule State Machine to simulate LIFO line management.
# Result: O(N) single-pass simulation with O(1) state transitions.

# Initialize the Side Space (LIFO Stack)
side_stack = []

# Time Complexity: O(1)
N = int(sys.stdin.readline())

# Time Complexity: O(N) to read and map the input sequence
waiting_stack = list(map(int, sys.stdin.readline().split()))

# [CRITICAL OPTIMIZATION] O(1) Queue Processing
# Reason: Standard pop(0) from the front of a list is O(N) because it forces the computer to shift 
# all remaining elements forward in memory. Reversing the list turns the "front" into the "back", 
# allowing us to use standard pop() which is a lightning-fast O(1) operation.
waiting_stack.reverse()

cnt = 1

# Time Complexity: O(N) overall. Each student is pushed/popped a maximum of two times.
while waiting_stack or side_stack:
    
    # Rule 1: The target person is at the front of the main line.
    # [CRITICAL GUARD] We must check `if waiting_stack` before accessing index [-1] to prevent an IndexError.
    if waiting_stack and waiting_stack[-1] == cnt:
        waiting_stack.pop() # O(1) removal
        cnt += 1
    
    # Rule 2: The target person is at the top of the side stack.
    # [CRITICAL GUARD] Verify `side_stack` exists before checking the top element.
    elif side_stack and side_stack[-1] == cnt:
        side_stack.pop() # O(1) removal
        cnt += 1
    
    # Rule 3: The target is not immediately available. 
    # We MUST move the person from the main line into the side stack.
    elif waiting_stack:
        side_stack.append(waiting_stack.pop()) # O(1) transfer
    
    # Rule 4: The main line is empty, and the top of the side stack is NOT the target.
    # The simulation is permanently deadlocked. Escape the loop.
    else:
        break

# Final Validation: If the side stack still has people inside, they are trapped.
if side_stack:
    print('Sad')
else:
    print('Nice')    