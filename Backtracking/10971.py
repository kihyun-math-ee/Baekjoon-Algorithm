import sys

target = []
N = int(sys.stdin.readline())
visit = [False] * N
L = [] 
m = float('inf')
cost = 0

def TSP(current, n, l):
    global m
    global cost
    global visit
    if len(target) == n - 1:
        if l[current][0] != 0:
            cost = sum(target) + l[current][0]
            if m > cost:
                m = cost
        return
    else:
        for j in range(n):
            if current != j:
                if visit[j] is False and l[current][j] != 0: 
                    target.append(l[current][j])
                    visit[j] = True
                    TSP(j, n, l)
                    target.pop()
                    visit[j] = False

for _ in range(N):
    rows = list(map(int, sys.stdin.readline().split()))
    L.append(rows)

visit[0] = True
TSP(0, N, L)
print(m)