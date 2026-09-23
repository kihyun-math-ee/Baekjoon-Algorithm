import sys
import math

A, B = map(int, sys.stdin.readline().split())
LCM = (A * B) // math.gcd(A, B)
print(LCM)