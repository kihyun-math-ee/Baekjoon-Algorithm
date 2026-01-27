import sys
A, B, C = map(int, sys.stdin.readline().split())
if A == B == C:
    print(10000+A*1000)
elif A == B and B != C:
    print(1000+A*100)
elif B == C and C != A:
    print(1000+B*100)
elif C == A and A != B:
    print(1000+C*100)
elif A < B < C:
    print(C*100)
elif B < A < C:
    print(C*100)
elif A < C < B:
    print(B*100)
elif C < A < B:
    print(B*100)
elif C < B < A:
    print(A*100)
else:
    print(A*100)