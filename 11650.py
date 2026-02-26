import sys

N = int(sys.stdin.readline())
list_total = [] 

for _ in range(N):
    list_xy = list(map(int, sys.stdin.readline().split()))
    list_total.append(list_xy)

sort_list = sorted(list_total)

for point in sort_list:
    print(*point)

    
    