import sys

# [Track B] Stack-based Bracket Validation
# Features: Validates correct pairing of brackets using a Last-In-First-Out (LIFO) structure.
# Time Complexity: O(L), where L is the length of s_list. Each character is pushed/popped at most once.
# Space Complexity: O(L) in the worst case (e.g., all opening brackets), used by the stack.
def is_valid(s_list):
    stack = []
    for char in s_list:
        if char in ['(', '{', '[']:
            stack.append(char)
        else:
            if not stack:
                return False
            else:
                if char == ')' and stack[-1] == '(':
                    stack.pop()
                elif char == '}' and stack[-1] == '{':
                    stack.pop()
                elif char == ']' and stack[-1] == '[':
                    stack.pop()
                else:
                    return False
    
    if not stack:
        return True
    else:
        return False

# [Track B] Brute-Force Single Bracket Substitution
# Implementation Principle: 
# 1. First, check if the original string is already valid.
# 2. If not, iterate through every character in the string.
# 3. For each position, try substituting it with every other possible bracket (5 alternatives).
# 4. Check validity using `is_valid`. Stop early if a valid string is found.
# Time Complexity: O(N * L^2), where N is the number of test cases and L is the length of string S.
#                  The outer loop runs L times, inner loop runs 5 times, and `is_valid` takes O(L) time. 
#                  Total operations per test case ≈ 5 * L^2.
def solve():
    N = int(sys.stdin.readline())
    for _ in range(N):
        S = sys.stdin.readline().strip()

        if is_valid(list(S)):
            print('YES', 0)
            continue

        brackets = ['(', '{', '[', ')', '}', ']']
        s_list = list(S)
        found = False

        for i in range(len(S)):
            original_char = s_list[i]

            for b in brackets:
                if original_char == b:
                    continue

                s_list[i] = b

                if is_valid(s_list):
                    print('YES', 1)
                    print(i+1, b)
                    found = True
                    break

            s_list[i] = original_char

            if found:
                break

        if not found:
            print('NO')

if __name__ == '__main__':
    solve()