import sys

numbers = set()

for _ in range(10):
    n = int(sys.stdin.readline())
    numbers.add(n % 42)

print(len(numbers))
