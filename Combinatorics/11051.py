import sys

N, K = map(int, sys.stdin.readline().split())
numerator = 1
denominator = 1

for i in range(K + 1, N + 1):
    numerator *= i
    
for j in range(1, N - K + 1):
    denominator *= j
    
result = (numerator // denominator) % 10007
print(result)