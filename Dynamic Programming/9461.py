import sys

f = [0] * 101
f[1] = f[2] = f[3] = 1
f[4] = f[5] = 2
for i in range(6, 101):
    f[i] = f[i - 1] + f[i - 5]
    
N = int(sys.stdin.readline())
for _ in range(N):
    target = int(sys.stdin.readline())
    print(f[target])
