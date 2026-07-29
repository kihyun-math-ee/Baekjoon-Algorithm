import sys

M = float('-inf')
m = float('inf')
def operator(d, current, plus, minus, mult, div):
    global M
    global m
    if d == N:
        if current > M:
            M = current
        if current < m:
            m = current
        return
    
    else:
        if plus != 0:
            operator(d + 1, current + target[d], plus - 1, minus, mult, div)
        if minus != 0:
            operator(d + 1, current - target[d], plus, minus - 1, mult, div)
        if mult != 0:
            operator(d + 1, current * target[d], plus, minus, mult - 1, div)
        if div != 0:
            operator(d + 1, int(current / target[d]) , plus, minus, mult, div - 1)

N = int(sys.stdin.readline())
target = list(map(int, sys.stdin.readline().split()))
pl, mi, mu, di = map(int, sys.stdin.readline().split())
operator(1, target[0], pl, mi, mu, di)
print(M)
print(m)