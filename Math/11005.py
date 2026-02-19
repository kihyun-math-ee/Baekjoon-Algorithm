import sys

N, B = map(int, sys.stdin.readline().split())

system = "0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ"
result = []

while N > 0:
    remainder = N % B
    N = N // B
    result.append(system[remainder])

print("".join(result[::-1]))
