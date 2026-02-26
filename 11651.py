import sys

N = int(sys.stdin.readline())
list_total = []

for _ in range(N):
    list_xy = list(map(int, sys.stdin.readline().split()))
    list_xy[0], list_xy[1] = list_xy[1], list_xy[0]
    list_total.append(list_xy)

S = sorted(list_total)

for j in range(N):
    print(S[j][1], S[j][0])