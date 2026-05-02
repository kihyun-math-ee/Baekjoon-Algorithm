import sys

N = int(sys.stdin.readline())
target = 1
for i in range(N, 0, -1):
    target *= i
    while target % 10 == 0:
        target //= 10
    target %= 100000000

result = str(target).zfill(5)[-5:]
print(result)
