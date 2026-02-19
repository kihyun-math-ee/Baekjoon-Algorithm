import sys
while True:
    M, N = map(int, sys.stdin.readline().split())
    if M == 0 and N == 0:
        break
    elif M % N == 0:
        print("multiple")
    elif N % M == 0:
        print("factor")
    else:
        print("neither")
