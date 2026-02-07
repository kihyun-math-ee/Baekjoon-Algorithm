import sys

num1, num2 = sys.stdin.readline().split()
reversed_max = max(int(num1[::-1]), int(num2[::-1]))
print(reversed_max)