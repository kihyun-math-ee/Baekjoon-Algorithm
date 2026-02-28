import sys

N = int(sys.stdin.readline())
sequence = str(N)
S = sorted(sequence, reverse = True)
print("".join(S))