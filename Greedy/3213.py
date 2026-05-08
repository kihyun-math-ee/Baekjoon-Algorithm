import sys
import math

a = 0
b = 0
c = 0
result = 0
N = int(sys.stdin.readline())

for _ in range(N):
    target = sys.stdin.readline().strip()
    
    if target == '1/4':
        a += 1
    elif target == '1/2':
        b += 1
    else:
        c += 1

a = max(0, a - c)
if b % 2 == 0:
    result = c + b//2 + math.ceil(a/4)
else:
    result = c + b//2 + math.ceil((a-2)/4) + 1

print(result)