import sys
import math
A, B, V = map(int, sys.stdin.readline().split())
T_initial = ((V-A)/(A-B))
ceiled_result = math.ceil(T_initial)
print(ceiled_result + 1)


