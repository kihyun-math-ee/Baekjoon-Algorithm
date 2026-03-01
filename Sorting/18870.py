import sys

N = int(sys.stdin.readline())
coordinates = list(map(int, sys.stdin.readline().split()))
unique_sorted = sorted(list(set(coordinates)))
rank_dict = {}

for i in range(len(unique_sorted)):
    rank_dict[unique_sorted[i]] = i

for num in coordinates:
    print(rank_dict[num], end=' ')
    





