import sys
import math

n, m = map(int, sys.stdin.readline().split(':'))
divisor = math.gcd(n, m)
print(f"{n // divisor}:{m // divisor}")