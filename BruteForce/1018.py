import sys

# BOJ 1018: Chessboard Repainting
# Category: Brute Force (Sliding Window)
# Time Complexity: O(N * M) 
#   - Outer Loops: Iterate (N-7)*(M-7) positions
#   - Inner Loops: Iterate constant 64 times (8x8)
#
# Engineering Notes:
# 1. The approach is a "2D Sliding Window". We slide an 8x8 frame across the NxM board.
# 2. There are only two valid chessboard patterns:
#    - Pattern A: Starts with 'W' at (0,0)
#    - Pattern B: Starts with 'B' at (0,0)
# 3. Instead of hardcoding patterns, we use Coordinate Parity:
#    - If (row + col) is Even: Color must match the Start Color.
#    - If (row + col) is Odd: Color must match the Opposite Color.

N, M = map(int, sys.stdin.readline().split())
board = []

# 1. Read the Input Board
# Note: readline() includes '\n', but strings are array-like so board[i][j] works fine.
for _ in range(N):
    board.append(sys.stdin.readline())

min_repaints = 64 # Initialize with max possible errors (8x8 = 64)

# 2. Sliding Window Loop (Move the Top-Left corner of the 8x8 frame)
# Range is N-7 because an 8x8 frame starting at N-7 would go out of bounds.
for y in range(N - 7):
    for x in range(M - 7):
        
        count_W = 0 # Repaints needed if top-left (0,0) is 'W'
        count_B = 0 # Repaints needed if top-left (0,0) is 'B'

        # 3. Internal Scanner (Check every cell inside the 8x8 frame)
        for i in range(y, y + 8):
            for j in range(x, x + 8):
                
                # Logic: Check if the current cell matches the expected color rule
                if (i + j) % 2 == 0:
                    # Even indices: Should match the Start Color
                    if board[i][j] != 'W': count_W += 1
                    if board[i][j] != 'B': count_B += 1
                else:
                    # Odd indices: Should match the Opposite Color
                    if board[i][j] != 'B': count_W += 1
                    if board[i][j] != 'W': count_B += 1
        
        # 4. Optimization: Update global minimum immediately after checking one frame
        min_repaints = min(min_repaints, count_W, count_B)

print(min_repaints)