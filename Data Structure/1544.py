import sys
from collections import deque

# [Data Structure 1] Hash Table (set)
# Utilized a hash set for O(1) time complexity in duplicate validation.
target = set()
N = int(sys.stdin.readline())
cnt = 0

for _ in range(N):
    S = sys.stdin.readline().strip()
    
    # O(1) search using the hash table
    if S not in target:
        # [Data Structure 2] Deque (Double-Ended Queue)
        # Converted to deque to achieve O(1) rotation via pointer manipulation, avoiding O(L) string slicing overhead.
        Q = deque(S)
        target.add(S)
        
        # Generate all possible cyclic combinations and register them to the hash set
        for _ in range(len(S)):
            Q.rotate(1)             
            # O(1) rotation
            target.add("".join(Q))  
            # Convert back to an immutable string for hashing
            
        cnt += 1

print(cnt)