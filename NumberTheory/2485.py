import sys
import math

N = int(sys.stdin.readline())
list_coordinates = []
list_coordinates_distance = []

for _ in range(N):
    coordinate = int(sys.stdin.readline())
    list_coordinates.append(coordinate)

for i in range(N - 1):
    list_coordinates_distance.append(list_coordinates[i + 1] - list_coordinates[i])

min_coordinate_distance = math.gcd(*list_coordinates_distance)
max_trees_gaps = (list_coordinates[-1] - list_coordinates[0]) // min_coordinate_distance
plant_trees = (max_trees_gaps + 1) - len(list_coordinates)

print(plant_trees)