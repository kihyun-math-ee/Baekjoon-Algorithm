import sys

target = []
houses = []
chickens = []
minimum = float('inf')
minimum_chick = 0
chick_distance = []

def chicken_backtracking(n, m, start):
    global minimum
    global minimum_chick
    if len(target) == m:
        distance_calculator(target)
        return
    
    for i in range(start, n):
        target.append(chickens[i])
        chicken_backtracking(n, m, i + 1)
        target.pop()

def distance_calculator(x):
    global minimum
    global minimum_chick
    for h in houses:
        for chick in x:
            if abs(h[0] - chick[0]) + abs(h[1] - chick[1]) < minimum:
                minimum = abs(h[0] - chick[0]) + abs(h[1] - chick[1])
        minimum_chick += minimum
        minimum = float('inf')
    chick_distance.append(minimum_chick)
    minimum_chick = 0

N, M = map(int, sys.stdin.readline().split())
for row in range(N):
    information = list(map(int, sys.stdin.readline().split()))
    for column in range(len(information)):
        if information[column] == 1:
            houses.append((row + 1, column + 1))
        elif information[column] == 2:
            chickens.append((row + 1, column + 1))

chicken_backtracking(len(chickens), M, 0)
print(min(chick_distance))