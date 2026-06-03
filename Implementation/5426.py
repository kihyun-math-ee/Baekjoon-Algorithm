import sys
import math

N = int(sys.stdin.readline())
for _ in range(N):
    S = sys.stdin.readline().strip()
    n = int(math.sqrt(len(S)))
    L = []
    for j in range(n):
        L.append(S[n-1-j::n])

    print(''.join(L))
        
