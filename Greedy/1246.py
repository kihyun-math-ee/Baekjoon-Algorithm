import sys

N, M = map(int, sys.stdin.readline().split())
L = []
S = 0
P = 0

for _ in range(M):
    affordable = int(sys.stdin.readline())
    L.append(affordable)

L.sort()

for i in range(M):
    sales_count = min(N, M - i)
    current_profit = sales_count * L[i]
    if current_profit > S:
         S = current_profit
         P = L[i]

print(P, S)