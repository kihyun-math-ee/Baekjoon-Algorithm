import sys

# BOJ 3986: Good Words (Stack Data Structure / String Manipulation)
# Time Complexity: O(N * L) where N is the number of words and L is the length of the string.
#
# Engineering Notes:
# 1. Utilizes a Stack (LIFO Data Structure) to pair matching consecutive letters.
# 2. Employs "Explosion Logic": If an incoming letter matches the top of the stack, 
#    they form a non-crossing connection and cancel out (pop).
# 3. Critical State Management: The stack MUST be explicitly re-initialized (Stack = []) 
#    at the start of every loop iteration to prevent "State Leaks" (garbage data carrying over).

N = int(sys.stdin.readline())
good_word_cnt = 0

for _ in range(N):
    # Read the word and strip the hidden newline character
    S = sys.stdin.readline().strip()
    
    # Re-initialize an empty stack for EVERY new word to prevent State Leaks
    Stack = [] 
    
    for i in range(len(S)):
        
        # Condition 1: If the stack is completely empty, we must push the current letter.
        if not Stack:
            Stack.append(S[i])
        
        else:
            # Condition 2: EXPLOSION LOGIC
            # If the incoming letter perfectly matches the top of the stack,
            # they form a valid pair and are removed from the stack.
            if S[i] == Stack[-1]:
                Stack.pop()
            
            # Condition 3: If they do not match, the new letter is added to the top.
            else:
                Stack.append(S[i])

    # At the end of the word iteration, if the stack is completely empty, 
    # every single letter successfully found a pair without crossing lines.
    if not Stack:
        good_word_cnt += 1

# Print the final count of validated Good Words
print(good_word_cnt)