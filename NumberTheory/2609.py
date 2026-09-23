import sys
import math

N, M = map(int, sys.stdin.readline().split())
print(math.gcd(N, M))
print(math.lcm(N, M))