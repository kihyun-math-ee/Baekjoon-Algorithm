import sys
T = int(sys.stdin.readline())

for _ in range(T):
    data = sys.stdin.readline().split()
    R = int(data[0])
    S = data[1]

    for x in S:
        print(x * R, end='') 
    print()