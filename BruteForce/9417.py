import sys
import math
N = int(sys.stdin.readline())

for _ in range(N):
    max_val = 0
    numbers = list(map(int, sys.stdin.readline().split()))
    
    for i in range(len(numbers) - 1):
        for j in range(i + 1, len(numbers)):
            if math.gcd(numbers[i], numbers[j]) > max_val:
                max_val = math.gcd(numbers[i], numbers[j])
    
    print(max_val)