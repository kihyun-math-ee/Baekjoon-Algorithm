import sys
import math

class Snail_climb:
    def __init__(self):
        None

    def climb_formula(self, A, B, V):
        self.result = math.ceil((V - A) / (A - B)) + 1
        print(self.result)

if __name__ == "__main__":
    my_snail_climb = Snail_climb()
    climb, slip, height = map(int, sys.stdin.readline().split())
    my_snail_climb.climb_formula(climb, slip, height)

