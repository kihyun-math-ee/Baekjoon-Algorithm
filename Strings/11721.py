import sys

S = sys.stdin.readline().strip()
N = (len(S) // 10) + 1

for i in range(N - 1):
    print(S[10*i : 10*(i+1)])

print(S[10*(N-1) :])

