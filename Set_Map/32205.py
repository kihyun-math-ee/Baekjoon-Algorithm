import sys

N = int(sys.stdin.readline())
S = set()

for _ in range(N):
    A, B, C = map(int, sys.stdin.readline().split())
    if A in S or B in S or C in S:
        print(1)
        sys.exit(0)
    else:
        S.add(A)
        S.add(B)
        S.add(C)
print(0)
                    


