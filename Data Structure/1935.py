import sys

# Read the number of operands (N)
N = int(sys.stdin.readline())
# Read the postfix expression string and strip the hidden newline character
S = sys.stdin.readline().strip()

# Initialize a dictionary to map alphabet characters to inputted numbers
operands_dict = {}
idx = 0
# Initialize an empty list to act as our Stack (LIFO structure) for holding operands
L_S = []
# Temporary list to handle the LIFO nature of the stack and reverse the popped operands
temp_L = []
alphabet = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'

# 1. Mapping Operands
# Time Complexity: O(N)
# We sequentially map each alphabet (A, B, C...) to the corresponding inputted numbers.
for i in range(N):
    num = int(sys.stdin.readline())
    operands_dict[alphabet[i]] = num

# 2. Evaluating the Postfix Expression
# Time Complexity: O(L), where L is the length of the string 'S'.
# We sweep through the postfix expression exactly once from left to right.
for j in range(len(S)):
    
    # Condition 1: It's an Operand (Alphabet A~Z).
    # We push its mapped number from the dictionary to the stack.
    if S[j] in alphabet:
        L_S.append(operands_dict[S[j]])

    # Condition 2: It's an Operator (*, /, +, -).
    # We must pop two operands, calculate, and push the result back to the stack.
    else:
        # Note: Due to Stack's LIFO (Last-In-First-Out) property, 
        # the first pop is the RIGHT operand, and the second pop is the LEFT operand.
        if S[j] == '*':
            temp_L.append(L_S.pop()) # temp_L[0] = Right Operand
            temp_L.append(L_S.pop()) # temp_L[1] = Left Operand
            
            # Execute the operation using the reversed order to match the original expression.
            L_S.append(temp_L[1] * temp_L[0])
            # Clear the temporary list for the next operation.
            temp_L.clear()

        elif S[j] == '/':
            temp_L.append(L_S.pop())
            temp_L.append(L_S.pop())
            L_S.append(temp_L[1] / temp_L[0])
            temp_L.clear()

        elif S[j] == '+':
            temp_L.append(L_S.pop())
            temp_L.append(L_S.pop())
            L_S.append(temp_L[1] + temp_L[0])
            temp_L.clear()

        elif S[j] == '-':
            temp_L.append(L_S.pop())
            temp_L.append(L_S.pop())
            L_S.append(temp_L[1] - temp_L[0])
            temp_L.clear()    

# 3. Final Output
# The final calculated result is the only remaining element in the stack.
result = L_S[0]
# Print the final result formatted strictly to 2 decimal places.
print(f"{result:.2f}")



    
 