import sys
import math

N = int(sys.stdin.readline())
list_coordinates = []
list_coordinates_distance = []
cnt = 0

for _ in range(N):
    coordinate = int(sys.stdin.readline())
    list_coordinates.append(coordinate)

for i in range(N - 1):
    list_coordinates_distance.append(list_coordinates[i + 1] - list_coordinates[i])

min_coordinate_distance = math.gcd(*list_coordinates_distance)
max_trees = (list_coordinates[-1] - list_coordinates[0]) // min_coordinate_distance

for j in range(max_trees):
    if list_coordinates[0] + (j * min_coordinate_distance) not in list_coordinates:
        cnt += 1

print(cnt)