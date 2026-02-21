import sys

A = int(sys.stdin.readline())
B = int(sys.stdin.readline())
C = int(sys.stdin.readline())

if A + B + C == 180 and A == B == C :
    print("Equilateral")

elif A + B + C == 180 and (A == B or B == C or C == A):
    print("Isosceles")

elif A + B + C == 180:
    print("Scalene")

else:
    print("Error")