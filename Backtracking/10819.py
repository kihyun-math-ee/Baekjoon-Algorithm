import sys

M = -1
target = []
S = 0
num = set()

def Taxicab(n, a):
    global M
    global S
    if len(target) == n:
        for i in range(n - 1):
            S += abs(target[i] - target[i + 1])
        if S > M:
            M = S
        S = 0
        return
    
    for j in range(n):
        if j not in num:
            target.append(a[j])
            num.add(j)
            Taxicab(n, a)
            target.pop()
            num.remove(j)

N = int(sys.stdin.readline())
A = list(map(int, sys.stdin.readline().split()))
Taxicab(N, A)

print(M)