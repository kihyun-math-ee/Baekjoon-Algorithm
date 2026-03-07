import sys
import math

n1, d1 = map(int, sys.stdin.readline().split())
n2, d2 = map(int, sys.stdin.readline().split())

raw_numerator = (n1 * d2) + (n2 * d1)
raw_denominator = d1 * d2

common_divisor = math.gcd(raw_numerator, raw_denominator)

print(raw_numerator // common_divisor, raw_denominator // common_divisor)