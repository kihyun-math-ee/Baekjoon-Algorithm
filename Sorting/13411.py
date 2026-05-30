import sys
import math

N = int(sys.stdin.readline())
time_list = []

for i in range(1, N + 1):
    X, Y, V = map(int, sys.stdin.readline().split())
    T = (math.sqrt((X**2) + (Y**2))) / V
    time_list.append((T, i))

time_list.sort()

for j in range(N):
    print(time_list[j][1])