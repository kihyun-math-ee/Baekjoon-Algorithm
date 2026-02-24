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
# 3. Instead of hardcoding patterns, we use Coordinate Parity with "Positive Logic":
#    - If (row + col) is Even: It MUST be the Start Color. (If not, it's an error).
#    - If (row + col) is Odd: It MUST be the Opposite Color. (If not, it's an error).

N, M = map(int, sys.stdin.readline().split())
board = []

# 1. Read the Input Board
for _ in range(N):
    board.append(sys.stdin.readline())

min_repaints = 64 # Initialize with max possible errors (8x8 = 64)

# 2. Sliding Window Loop (Move the Top-Left corner of the 8x8 frame)
for y in range(N - 7):
    for x in range(M - 7):
        
        count_W = 0 # Case 1: Top-Left (0,0) starts White
        count_B = 0 # Case 2: Top-Left (0,0) starts Black

        # 3. Internal Scanner (Check every cell inside the 8x8 frame)
        for i in range(y, y + 8):
            for j in range(x, x + 8):
                
                # Logic: Check if the current cell matches the expected color rule
                if (i + j) % 2 == 0:
                    # Even indices: Should match the Start Color
                    if board[i][j] == 'B': 
                        count_W += 1 # Error! Wanted White, got Black
                    if board[i][j] == 'W': 
                        count_B += 1 # Error! Wanted Black, got White
                else:
                    # Odd indices: Should match the Opposite Color
                    if board[i][j] == 'W':
                        count_W += 1 # Error! Wanted Black (Opposite), got White
                    if board[i][j] == 'B':
                        count_B += 1 # Error! Wanted White (Opposite), got Black
        
        # 4. Optimization: Update global minimum immediately after checking one frame
        # CRITICAL: This must be inside the 'x' loop, but outside the 'i/j' loops.
        min_repaints = min(min_repaints, count_W, count_B)

print(min_repaints)