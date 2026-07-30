import sys

N = int(sys.stdin.readline())
distance = list(map(int, sys.stdin.readline().split()))
city = list(map(int, sys.stdin.readline().split()))
m = city[0]
minimum_result = m * distance[0]

for i in range(1, N - 1):
    if m > city[i]:
        m = city[i]
    minimum_result += m * distance[i]

print(minimum_result)