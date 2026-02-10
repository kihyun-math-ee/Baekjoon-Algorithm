import sys

# 1. Initialize Stacks
# left_stack holds the initial string
left_stack = list(sys.stdin.readline().strip())
right_stack = []

# 2. Command Processing
M = int(sys.stdin.readline())

for _ in range(M):
    cmd = sys.stdin.readline().split()
    
    if cmd[0] == 'L':
        # Move Left: Pop from Left, Push to Right
        if left_stack:
            right_stack.append(left_stack.pop())
            
    elif cmd[0] == 'D':
        # Move Right: Pop from Right, Push to Left
        if right_stack:
            left_stack.append(right_stack.pop())
            
    elif cmd[0] == 'B':
        # Backspace: Delete from Left
        if left_stack:
            left_stack.pop()
            
    elif cmd[0] == 'P':
        # Insert: Push to Left
        left_stack.append(cmd[1])

# 3. Final Merge
# Right stack is in reverse order (LIFO), so flip it back
right_stack.reverse()
print(*(left_stack + right_stack), sep='')