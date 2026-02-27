import sys

n = int(sys.stdin.readline())
stack = []
result = []      # Save answers here instead of printing
current = 1      # The numbers 1, 2, 3, 4... we push into the stack
is_possible = True

for _ in range(n):
    target_num = int(sys.stdin.readline()) # Just get the next number we need
    
    # RULE 1: Catch up to the target_num
    # If our current number is 1, and the target_num is 4...
    # We must push 1, 2, 3, 4 into the stack.
    while current <= target_num:
        stack.append(current)
        result.append("+")
        current += 1
        
    # RULE 2: Now that we caught up, the top of the stack SHOULD be target_num
    if stack[-1] == target_num:
        stack.pop()
        result.append("-")
        
    # RULE 3: If the top of the stack is NOT target_num... it's impossible!
    else:
        is_possible = False
        break # Break the loop!

# FINAL OUTPUT
if is_possible == False:
    print("NO")
else:
    # Print everything in the result list cleanly
    print('\n'.join(result))

