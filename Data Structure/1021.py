import sys
from collections import deque

N, M = map(int, sys.stdin.readline().split())
my_deque = deque(range(1, N + 1))
target_list = list(map(int, sys.stdin.readline().split()))
cost_min = 0

for target in target_list:
    target_index = my_deque.index(target)

    halfway = len(my_deque) // 2

    if target_index <= halfway:
        my_deque.rotate(-target_index)
        cost_min += target_index
    else:
        spins_needed = len(my_deque) - target_index
        my_deque.rotate(spins_needed)
        cost_min += spins_needed

    my_deque.popleft()

print(cost_min)
